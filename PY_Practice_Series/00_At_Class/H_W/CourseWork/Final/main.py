import os as s
from operation import (
    get_refined_user_purchased_info, 
    user_purchased_full_data, 
    generate_purchased_invoices, 
    get_refined_user_return_info, 
    user_return_full_data, 
    generate_returned_invoices
)
from read import show_only_values, data_into_list
from write import (
    write_generated_invoice_to_file, 
    save_modified_data_to_file, 
    write_generated_return_invoice_to_file
)

def main():
    """
    Display a menu for managing land transactions, allowing users to:
    1. View and manage purchased land.
    2. Return previously purchased land.
    3. Exit the program.
    """
    try:
        print("""
              ▀█▀ █▀▀ █▀▀ █ █ █▄ █ █▀█        █▄ █ █▀▀ █▀█ █▀█ █
               █  ██▄ █▄▄ █▀█ █ ▀█ █▄█   ░░   █ ▀█ ██▄ █▀▀ █▀█ █▄▄
                            \\_______________________/
                               \\__Ｗｅｌｃｏｍｅ__/
                                    \\_______/
                                       \\  /
                    ┌──────────────────────────────────────┐
                    │        ╭──────────────────╮          │
                    │        │     L A N D S     │         │
                    │        ╰──────────────────╯          │
                    │    ➤ 1. 🌄 Rent Land                .│
                    |        -------------------           |
                    │    ➤ 2. 🔄 Return Land              .│
                    |        -------------------           |
                    │    ➤ 3. 👀 Show Lands               .│
                    |        -------------------           |
                    │    ➤ 4. 🚪 Exit                      │
                    └──────────────────────────────────────┘
        """)
        # Get user choice
        user_choice = validation(input("Please choose an option from the menu: \n"))
         # Create necessary directories
        create_directories()

        # Perform actions based on user choice
        if user_choice == 1:
            purchased_land()
        elif user_choice == 2:
            returned_land()
        elif user_choice == 3:
            show_lands()
        elif user_choice == 4:
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please choose a number between 1 and 3.")
            main()
    except Exception as e:
        print("An error occurred:", e)
        main()



def validation(user_choice):
    """
    Validate user input to ensure it's a number.
    
    Args:
    - user_choice (str): The user's input.
    
    Returns:
    - int: The user's choice as an integer.
    """
    while not user_choice.isdigit():
        print("Sorry, that's not a valid choice. Please enter a number.")
        user_choice = input("Please choose an option from the menu: \n")
    return int(user_choice)


def create_directories():
    """
    Create folders to store invoices if they don't exist already.
    """
    directories = ['Invoices/purchased', 'Invoices/return']
    for directory in directories:
        try:
            if not s.path.exists(directory):
                s.makedirs(directory)
            else:
                pass
        except Exception as e:
            print(f"An error occurred while creating directory {directory}: {e}")


def show_lands():
    """
    Display a list of available lands with their details.
    """
    land_data = show_only_values()
    separator = "═" * 102 + "╗"
    print(separator)
    header = f"""|      {'KITTA NO':<10} | {'LOCATION':<20} | {'DIRECTION':<15} | {'ANNA':<10} | {'PRICE':<10} | {'AVAILABILITY':<15}|"""
    separator = "═" * (len(header)-1) + "|"

    print(header)
    print(separator)
    for record in land_data:
        kitta_no, location, direction, anna, price, availability = record
        print(f"""|      {kitta_no:<10} | {location:<20} | {direction:<15} | {anna:<10} | {price:<10} | {availability:<15}|""")

    # Displaying separator after records
    separator = "═" * 102 + "╝"
    print(separator)
    print()

    # Invoking further actions
    main()


def purchased_land():
    # Prompt user for confirmation
    # Prompt user for the choice to proceed with land rental
    while True:
        choice = input("Are you sure you want to proceed with land rental? (yes/press (Enter) for main menu): ").lower()
        if choice == '' or choice == 'yes':
            break
        else:
            print("🔺 Invalid choice. Please enter 'yes' or press (Enter) for the main menu.")

    if choice == "yes":
        # Proceed with land rental

        # Gather list of dict further process
        raw_datas = data_into_list()

        # Refine user information for purchased land
        user_information = get_refined_user_purchased_info()

        # Process user's purchased land data
        user_purchased_data_with_user_info, datas_to_write_into_data_txt = user_purchased_full_data(user_information, raw_datas)

        # Generate invoices for purchased land
        list_of_writable_invoices, allTotal_with_vat, allTotal, all_vat_amount = generate_purchased_invoices(user_purchased_data_with_user_info)
        if list_of_writable_invoices:
            # Write generated invoices to file
            write_generated_invoice_to_file(list_of_writable_invoices, user_information, allTotal_with_vat, allTotal, all_vat_amount)
            # Save modified data to file
            save_modified_data_to_file(datas_to_write_into_data_txt)

            # Extract land IDs and rental months for success message
            land_ids = ', '.join(user_information['land_data'].keys())
            months_per_land = ', '.join(str(month) for month in user_information['land_data'].values())
            print(f"\nCongratulations, {user_information['name']}! You've successfully Rented Kitta No:\n\t{land_ids}\n\tFor {months_per_land} Months 🐱‍👤🤩")
        else:
            # No data found for purchase
            print("\nEmpty Data Found Can't purchased ! ")
        main()
    else:
        # Go back to main menu if user presses Enter or enters anything else
        print("\nGoing back to main menu.")
        main()




def returned_land():
    """
    Handles the process of returning land.

    Prompts the user for confirmation, processes return data,
    generates return invoices, writes data and invoices to files,
    and displays a success message upon successful return.
    """
    
    # Prompt user for confirmation before proceeding with land return
    # Prompt user for the choice to continue with the land return process
    while True:
        choice = input("Are you sure to continue with the land return process? (yes/press (Enter) for main menu): ").lower()
        if choice == '' or choice == 'yes':
            break
        else:
            print("🔺 Invalid choice. Please enter 'yes' or press (Enter) for the main menu.")

    if choice == "yes":
        # Proceed with land return
        
        # Gather list of dict further process
        raw_datas = data_into_list()
        
        # Refine user information for returned land
        user_information = get_refined_user_return_info()
        
        # Process user's returned land data
        user_return_data_with_user_info, returned_datas_to_write_into_data_txt = user_return_full_data(user_information, raw_datas)
        
        # Generate return invoices for returned land
        list_of_returnable_invoices, all_total, allTotal_with_vat, all_vat_amount, all_fines, allTotal_with_fine = generate_returned_invoices(user_return_data_with_user_info)
        
        if list_of_returnable_invoices:
            # Invoices generated successfully
            
            # Write generated return invoices to file
            invoices = write_generated_return_invoice_to_file(list_of_returnable_invoices, user_information, all_total, allTotal_with_vat, all_vat_amount, all_fines, allTotal_with_fine)
            print(invoices)
            
            # Save modified data to file
            save_modified_data_to_file(returned_datas_to_write_into_data_txt)
            
            # Extract land IDs and rental months for success message
            land_ids = ', '.join(user_information['land_data'].keys())
            months_per_land = ', '.join(str(month) for month in user_information['land_data'].values())
            
            # Display success message with details of returned land
            print(f"\nCongratulations, {user_information['name']}! You've successfully Returned Kitta No:\n\t{land_ids}\n\tIn {months_per_land} Months 🐱‍👤🤩")
        else:
            # No data found for return
            print("\nEmpty Data Found. Can't proceed with land return!")
        
        # Return to the main menu
        main()
    else:
        # User decided not to proceed with land return
        
        # Go back to main menu 
        print("\nGoing back to main menu.")
        main()



if __name__ == "__main__":
    main()
