from read import *
import os as s
from datetime import datetime


def get_refined_user_purchased_info():
    """
    Function to gather and refine user information for land rental.

    Asks the user for their name, contact number, and land rental details,
    including kitta number(s) and number of months for each kitta.

    Returns a dictionary containing the refined user information.
    """
    user_data = {}

    # ++++++++++++++++++++++++++++++++++++ TAKING LAND KITTA NO AND MONTHS START +++++++++++++++++++++++++++++++++++++++++++++++++++++
    land_data = {}
    # Prompt user for multiple land rental or single land rental
    while True:
        purchase_multiple = input("\033[1m🟢 Do you want to Rent multiple lands? (yes/no): \033[0m").lower()
        if purchase_multiple in ['yes', 'no']:
            break
        else:
            print("🔺 Invalid choice. Please enter 'yes' or 'no'.")


    # Handle multiple land rental
    if purchase_multiple == 'yes':
        while True:
            land_id = input("\033[1m🌟 Enter a Kitta No (and press 'Enter' to finish): \033[0m")
            if land_id.lower() == '':
                break
            else:
                availability = purchasing_availability_check(land_id)
                if availability:
                    if land_id in land_data:
                        print(f"❌ You've already specified the duration for Kitta No {land_id}.")
                    else:
                        while True:
                            purchased_month = input(f"\033[1m📅 How many months would you like to rent this {land_id} kitta ?:  \033[0m")
                            if purchased_month.isdigit() and int(purchased_month) > 0:
                                land_data[land_id] = int(purchased_month)
                                break
                            else:
                                print("❌ Please enter a valid number of months.")
                else:
                    print(f"❌ This land {land_id} is not available in our records for purchase.")
    # Handle single land rental               
    elif purchase_multiple == 'no':
        while True:
            land_id = input("\033[1m🌟 Enter a Kitta No: \033[0m")
            availability = purchasing_availability_check(land_id)
            if availability:
                purchased_month = input(f"\033[1m📅 How many months would you like to rent this {land_id} kitta:  \033[0m")
                if purchased_month.isdigit() and int(purchased_month) > 0:
                    land_data[land_id] = int(purchased_month)
                    break  # Exit the loop if a valid Kitta No and number of months are provided
                else:
                    print("❌ Please enter a valid number of months.")
            else:
                print(f"❌ This land {land_id} is not available in our records for purchase.")
    else:
        print(f"🔺 Invalid choice {purchase_multiple}. Please enter 'yes' or 'no'.")
    # Store land rental details in user data
    user_data['land_data'] = land_data
    # ++++++++++++++++++++++++++++++++++++ TAKING LAND KITTA NO AND MONTHS END +++++++++++++++++++++++++++++++++++++++++++++++++++++
    # ++++++++++++++++++++++++++++++++++++ TAKING USER NAME START +++++++++++++++++++++++++++++++++++++++++++++++++++++
    while True:
        # Prompt user for their name
        name = input("👤 Enter your name: ")
        if name.strip():
            if not any(char.isdigit() for char in name):
                user_data['name'] = name
                break
            else:
                print(f"❌ The name {name} contains integers. Please enter a valid name.")
        else:
            print("🔺 Name cannot be empty. Please enter your name.")
    # ++++++++++++++++++++++++++++++++++++ TAKING USER NAME END +++++++++++++++++++++++++++++++++++++++++++++++++++++

    # ++++++++++++++++++++++++++++++++++++ TAKING USER CONTACT START +++++++++++++++++++++++++++++++++++++++++++++++++++++
    while True:
        # Prompt user for their contact number
        contact = input("📞 Enter your contact number: ")
        if contact.isdigit() and len(contact) == 10:
            user_data['contact'] = contact
            break 
        else:
            print("🔺 Invalid contact number. Please enter a 10-digit number.")
    # ++++++++++++++++++++++++++++++++++++ TAKING USER CONTACT END +++++++++++++++++++++++++++++++++++++++++++++++++++++

    return user_data



def purchasing_availability_check(entered_kitta):
    """
    Check the availability of the entered kitta number for purchase.

    Args:
        entered_kitta (str): The kitta number entered by the user.

    Returns:
        list: A list containing the entered kitta number if it's available for purchase,
              otherwise an empty list.
    """
    # Get data from the source (presumably a list of dictionaries)
    datas = data_into_list()

    # Iterate through the data to find the matching kitta number
    for data in datas:
        # Check if the kitta number matches and if it's available for purchase
        if data["id"] == entered_kitta and data["availability"] == "Available":
            # If available, return a list containing the kitta number
            return [entered_kitta]

    # If kitta number is not available or not found, return an empty list
    else:
        return []

# ________________________________________________PART 1 END___________________________________________



# ________________________________________________PART 2 START___________________________________________
# No ii
def user_purchased_full_data(user_info, raw_datas):
    """
    Process user's purchased land data and prepare it for writing.

    Args:
        user_info (dict): Dictionary containing user information including name, contact, and land rental details.
        raw_datas (list): List of dictionaries containing raw land data.

    Returns:
        tuple: A tuple containing two elements:
               - A list of dictionaries representing purchased land data with user information.
               - A list of dictionaries representing raw land data (unchanged).
    """
    purchased_list = []  # List to store processed purchased land data
    datas_to_write = raw_datas  # Store raw land data for writing (if no changes)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current timestamp

    # Iterate through raw land data to process purchased land data
    for data in datas_to_write:
        # Check if the land ID is present in user's purchased land data
        if str(data['id']) in user_info['land_data'].keys():
            # Extract relevant information from raw land data
            price = int(data['price'])
            purchased_month = user_info['land_data'][str(data['id'])]
            total = int(purchased_month) * price
            vatAmount, grandTotal = calculate_grand_total_and_vat(total)

            # Prepare remarks and update availability if land is available
            Remarks = "null"
            if data['availability'] == 'Available':
                data['availability'] = 'Not Available'

            # Create a dictionary containing processed purchased land data with user information
            data_with_user_info = {
                'id': data['id'],
                'location': data['location'],
                'direction': data['direction'],
                'Anna': data['anna'],
                'price': data['price'],
                'Remarks': Remarks,
                'name': user_info['name'],
                'contact': user_info['contact'],
                'months': purchased_month,
                'vat_amount': vatAmount,
                'Grand_Total': grandTotal,
                'Timestamp': timestamp,
                'duration': calculate_expiration_date(purchased_month),
                'total': total
            }

            # Append processed purchased land data to the list
            purchased_list.append(data_with_user_info)

    # Return the processed purchased land data and the raw land data
    return purchased_list, datas_to_write



def calculate_grand_total_and_vat(prices):
    """
    Calculate the VAT amount and grand total based on the given price.

    Args:
        prices (float): The total price before VAT calculation.

    Returns:
        tuple: A tuple containing two elements:
               - The VAT amount calculated based on the given price.
               - The grand total including the original price and VAT.
    """
    vat_percentage = 13  # VAT percentage
    vatAmount = (prices * vat_percentage) / 100  # Calculate VAT amount
    grand_total = prices + vatAmount  # Calculate grand total including VAT
    return vatAmount, grand_total




def calculate_expiration_date(month):
    """
    Calculate the expiration date based on the current date and the given number of months.

    Args:
        month (int): The number of months to add to the current date.

    Returns:
        str: A string representing the expiration date in "YYYY-MM-DD" format.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current timestamp
    date_expired = timestamp.split("-")  # Split timestamp into year, month, and day
    this_month = int(date_expired[1])  # Extract the current month
    exp_new_month = this_month + int(month)  # Calculate the new expiration month
    date_expired[1] = str(exp_new_month)  # Update the expiration month

    final_date = "-".join(date_expired)  # Join the components to form the final expiration date
    return final_date  # Return the expiration date

# ________________________________________________PART 2 END___________________________________________


# ________________________________________________PART 3 START___________________________________________
def generate_purchased_invoices(datas):
    """
    Generate invoices for purchased land.

    Args:
        datas (list): A list of dictionaries containing purchased land data.

    Returns:
        tuple: A tuple containing three elements:
               - A list of strings representing the generated invoices.
               - The total amount including VAT for all purchased land.
               - The total amount without VAT for all purchased land.
               - The total VAT amount for all purchased land.
    """
    invoices = []  # List to store generated invoices
    all_total = 0  # Variable to store the total amount without VAT
    allTotal_with_vat = 0  # Variable to store the total amount including VAT
    all_vat_amount = 0  # Variable to store the total VAT amount
    for item in datas:
        # Update total amounts and VAT amount
        all_vat_amount += float(item['vat_amount'])
        all_total += float(item['total'])
        allTotal_with_vat += float(item["Grand_Total"])
        invoice = f"""
                                    ICP Rental Pokhara
                                10, Hospital Chowk, Pokhara

Customer Details:                                                         Date: {item['Timestamp'].split()[0]}
Name: {item['name']}
Address: {item["location"]}
Phone: {item['contact']}

+---------------------+------------------+-------------+---------+----------+-----------------+
|     Kitaa Number    |    Location      |  Direction  |   Anna  | Price in Rs |   Remarks    |
+---------------------+------------------+-------------+---------+----------+-----------------+
|        {item['id']: <12} |   {item['location']: <14} |    {item['direction']: <8} |    {item['Anna']: <7} |  {item['price']: <10} | {item['Remarks']: <10}|
+---------------------+------------------+-------------+---------+----------+-----------------+

Total Rs: {item["total"]}
VAT (13%) Rs: {item['vat_amount']}
Grand Total Rs: {item['Grand_Total']}

Additional Data:
Months:            {item['months']: <20}              
Purchased Duration:    {item['duration']: <20}

=================================================================================================
"""
        invoices.append(invoice)    # Append generated invoice to the list
    # Return the generated invoices and total amounts
    return invoices, allTotal_with_vat, all_total, all_vat_amount

# ________________________________________________PART 3 END___________________________________________

# Purchased Part end
##################################################################################################################





# Return Part Start
###################################################################################################################

# ________________________________________________PART 1 START___________________________________________
def get_refined_user_return_info():
    """
    Get refined user information for returning land.

    Returns:
        dict: A dictionary containing user information including name, contact, and land return details.
    """
    
    user_data = {}

    # Get selected land data for return
    user_data['land_data'] = get_selected_return_land_data()
    
    # Prompt user for name
    while True:
        name = input("👤 Enter your name: ")
        status = check_filename(name)
        if name.strip():
            if status:
                user_data['name'] = name
                break
            else:
                print(f"❌ The user with name {name} hasn't purchased any land")
        else:
            print("❌ Name cannot be empty. Please enter your name.")

    # Prompt user for contact number
    while True:
        contact = input("📞 Enter your contact number: ")
        if contact.isdigit() and len(contact) == 10:
            user_data['contact'] = contact
            break 
        else:
            print("❌ Invalid contact number. Please enter a 10-digit number.")

    return user_data


def get_selected_return_land_data():
    """
    Get selected land kitta for return.

    Returns:
        dict: A dictionary containing land data selected for return, with kitta number as keys
              and return months as values.
    """
    land_data = {}
    # Prompt user for returning multiple land rentals or single land rental
    while True:
        return_multiple = input("\033[1m🟢 Do you want to return multiple lands? (yes/no): \033[0m").lower()
        if return_multiple in ['yes', 'no']:
            break
        else:
            print("🔺 Invalid choice. Please enter 'yes' or 'no'.")

    if return_multiple == 'yes':
        while True:
            # Prompt user to enter multiple kitta numbers for return
            land_id = input("\033[1m🌟 Enter a Kitta no (and press 'Enter' to finish): \033[0m")
            if land_id.lower() == '':
                break
            elif not land_id.isdigit():
                print("🔺 Invalid Kitta NO. Please enter a number.")
                continue
            
             # Check availability of land for return
            availability = checking_availability_of_return(land_id)
            if availability:
                if land_id in land_data:
                    print(f"❌ You've already selected Kitta No {land_id}.")
                else:
                    while True:
                        return_month = input(f"\033[1m📅 In How many months you have Return this {land_id} kitta: \033[0m")
                        if return_month.isdigit() and int(return_month) > 0:
                            land_data[land_id] = int(return_month)
                            break
                        else:
                            print("❌ Please enter a valid number of months.")
            else:
                print(f"❌ This land {land_id} is not available so, we can't return.")
                
    elif return_multiple == 'no':
        # Prompt user to enter a single kitta number for return
        while True:
            land_id = input("\033[1m🌟 Enter a Kitta No: \033[0m")
            availability = checking_availability_of_return(land_id)
            if availability:
                return_month = input(f"\033[1m📅 In How many months you have Return this {land_id} kitta  \033[0m")
                if return_month.isdigit() and int(return_month) > 0:
                    land_data[land_id] = int(return_month)
                    break  
                else:
                    print("❌ Please enter a valid number of months.")
            else:
                print(f"❌ This land {land_id} is not available in our records for return.")
    else:
        print("🔺 Invalid choice. Please enter 'yes' or 'no'.")

    return land_data



def checking_availability_of_return(land_id):
    """
    Check the availability of a land for return.

    Args:
        land_id (str): The ID of the land to check for availability.

    Returns:
        bool: True if the land is not available for return, False otherwise.
    """
    datas = data_into_list()  # Get list of land data
    for data in datas:
        # Check if the land ID matches and the land is not available
        if data['id'] == land_id and data['availability'] == 'Not Available':
            return True  # Land is  available for return

    return False  # Land is not available for return



def check_filename(user_name):
    """
    Check if a file exists in the purchased invoices directory with the user's name.

    Args:
        user_name (str): The name of the user to check for in file names.

    Returns:
        str or None: If a matching file is found, return the file name. Otherwise, return None.
    """
    file_path = "Invoices/purchased/"  # Path to the directory containing purchased invoices
    files = s.listdir(file_path)  # Get list of files in the directory

    for file_name in files:
        # Extract the name part from the file name
        name_part = file_name.split('_')[-1].split('Purchased.txt')[0]

        # Check if the extracted name part matches the user's name
        if user_name == name_part:
            return file_name  # Return the file name if a match is found
        
    return None  # Return None if no matching file is found


# ________________________________________________PART 1 END___________________________________________



# ________________________________________________PART 2 START___________________________________________

def user_return_full_data(user_info, raw_datas):
    """
    Process user return information and generate full return data.

    Args:
        user_info (dict): User information including name, contact, and land return details.
        raw_datas (list): List of raw land data to process.

    Returns:
        tuple: A tuple containing the list of processed return data and the original raw data.
    """
    returned_list = []
    datas_to_write = raw_datas
    month_purchased = grab_purchased_month(user_info)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    for data in datas_to_write:
        if str(data['id']) in user_info['land_data']:
            return_month = user_info['land_data'][str(data['id'])]
            
            # Check if the ID exists in month_purchased dictionary
            if int(data['id']) in month_purchased:
                purchased_month = month_purchased[int(data['id'])]
                fine = calculate_fine(return_month, purchased_month)
            else:
                # Handle the case where ID doesn't exist in month_purchased
                # Display a message indicating that the land was rented by another person
                print("\n\033[91m" + f"Land with ID {data['id']} was rented by another person." + "\033[0m")
                continue  # Skip processing this data entry
            
            Remarks = "null"
            if data['availability'] == 'Not Available':
                data['availability'] = 'Available'
                
            data_with_user_info = {
                'id': data['id'],
                'location': data['location'],
                'direction': data['direction'],
                'Anna': data['anna'],
                'price': data['price'],
                'Remarks': Remarks,
                'name': user_info['name'],
                'contact': user_info['contact'],
                'months': return_month,
                'fine': fine,
                'Timestamp' : timestamp
            }
            returned_list.append(data_with_user_info)
    
    return returned_list, datas_to_write


def grab_purchased_month(user_info):
    """
    Extracts the month of purchase for each land rented by the user.

    Args:
        user_info (dict): User information including name.

    Returns:
        dict: A dictionary mapping each land's ID to its month of purchase.
    """
    expiration_months = {}  # Dictionary to store land IDs and their respective purchase months
    kittano = None  # Placeholder for the current land ID being processed
    name = user_info["name"]  # Get the user's name from the user information
    file_paths = [file for file in s.listdir("Invoices/purchased/") if name in file]  # Get file paths containing user's name

    for file_name in file_paths:
        file_path = s.path.join("Invoices/purchased/", file_name)  # Construct file path
        with open(file_path, 'r') as file:
            for line in file:
                if "| null      |" in line:
                    # Extract the kittano (land ID) from the line
                    kittano = line.split("|")[1].strip()
                    kitta = int(kittano)  # Convert land ID to integer
                elif "Months:" in line and kittano is not None:
                    # Extract the purchased date from the line
                    purchased_date = line.split(":")[1].strip()
                    # Extract the month from the purchased date and store in dictionary
                    purchase_month = int(purchased_date)
                    expiration_months[kitta] = purchase_month
                    kittano = None  # Reset the land ID placeholder

    return expiration_months  # Return the dictionary mapping land IDs to purchase months



def calculate_fine(month_return, purchased_month):
    """
    Calculate the fine for late return of a rented land.

    Args:
        month_return (int): The month of return.
        purchased_month (int): The month of purchase.

    Returns:
        int: The fine amount for late return.
    """
    fine_per_month = 1000  # Fine amount per month for late return
    fines = 0  # Initialize fines variable
    
    if month_return > purchased_month:
        # Calculate the number of months overdue
        over_time = month_return - purchased_month
        # Calculate the total fines based on the number of months overdue
        fines = over_time * fine_per_month
    else:
        fines = 0  # No fines if return is on time
    
    return fines  # Return the calculated fines amount



# ________________________________________________PART 2 END___________________________________________




# ________________________________________________PART 3 START___________________________________________

def generate_returned_invoices(datas):
    """
    Generate invoices for returned lands including fines.

    Args:
        datas (list of dict): List of dictionaries containing returned land information.

    Returns:
        tuple: A tuple containing:
            - list: List of generated invoices.
            - float: Total amount without fines.
            - float: Total amount with VAT but without fines.
            - float: Total VAT amount.
            - float: Total fines amount.
            - float: Total amount including fines.
    """
    invoices = []            # List to store generated invoices
    all_total = 0            # Initialize total amount without fines
    allTotal_with_vat = 0    # Initialize total amount with VAT but without fines
    all_vat_amount = 0       # Initialize total VAT amount
    all_fines = 0            # Initialize total fines amount
    allTotal_with_fine = 0   # Initialize total amount including fines
    for item in datas:
        # Calculate total amount for the returned land
        price = float(item['price'])
        total = price * float(item['months'])
        all_total += total  # Update total amount without fines

        # Calculate VAT amount
        vat_amount = total * 0.13
        all_vat_amount += vat_amount  # Update total VAT amount

        # Calculate fine amount
        fine = float(item["fine"])
        all_fines += fine  # Update total fines amount

        # Calculate grand total with fines
        grand_total = total + vat_amount + fine
        allTotal_with_fine += grand_total  # Update total amount including fines

        # Calculate total amount with VAT but without fines
        allTotal_with_vat += (grand_total - fine)  # Update total amount with VAT but without fines
        
        invoice = f"""
                                ICP Rental Pokhara
                            10, Hospital Chowk, Pokhara

Customer Details:                                                     Date: {item['Timestamp'].split()[0]}
Name: {item['name']}
Address: {item["location"]}
Phone: {item['contact']}

+---------------------+------------------+-------------+---------+----------+-----------------+
|     Kitaa Number    |    Location      |  Direction  | Total Anna | Price in Rs |   Remarks |
+---------------------+------------------+-------------+---------+----------+-----------------+
|        {item['id']: <12} |   {item['location']: <14} |    {item['direction']: <8} |    {item['Anna']: <7} |  {item['price']: <10} | {item['Remarks']: <10}|
+---------------------+------------------+-------------+---------+----------+-----------------+

Total Rs: {total}                                                                      
VAT (13%) Rs: {vat_amount}
Grand Total Rs: {grand_total} (Included Fine)                                                FINE: {item['fine']}

Additional Data:
Months:            {item['months']: <20}              
Returned Date:    {item['Timestamp']: <20}

=================================================================================================
"""
        invoices.append(invoice)
    return invoices, all_total, allTotal_with_vat, all_vat_amount, all_fines, allTotal_with_fine
# ________________________________________________PART 3 END_____________________________________________