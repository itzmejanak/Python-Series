from datetime import datetime # have to introduce in cw doc

def save_modified_data_to_file(datas):
    """
    Save data to a text file.

    Args:
    - datas (list): A list of dictionaries representing the data to be saved.
    """
    with open("data.txt", 'w') as file:
        for data in datas:
            modified_data = ", ".join(data.values()) + "\n"
            file.write(modified_data)


def write_generated_invoice_to_file(list_of_writable_invoices, user_info, allTotal_withVat, allTotal_noVat, all_vat_amount):
    """
    Write generated invoices to a file.

    Args:
        list_of_writable_invoices (list): List of generated invoices as strings.
        user_info (dict): User information including name.
        allTotal_withVat (float): Total amount including VAT.
        allTotal_noVat (float): Total amount excluding VAT.
        all_vat_amount (float): Total VAT amount.
    """
    name = user_info["name"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    acceptable_timestamp = timestamp.replace(":", "_").replace(" ", "-")
    file_path = f"Invoices/purchased/{acceptable_timestamp}_{name}Purchased.txt"

    with open(file_path, 'w') as file:
        for invoice in list_of_writable_invoices:
            file.write(invoice + '\n\n')
            print(invoice + '\n\n')

    # Open the file again in append mode
    with open(file_path, 'a') as files:
        # Writing total information
        files.write("--------------\n")
        files.write("TOTAL SUMMARY\n")
        files.write("--------------\n")
        files.write(f"Total Amount (Excluding VAT): {allTotal_noVat}\n")
        files.write(f"Total VAT(13%) Amount: {all_vat_amount}\n")
        files.write(f"Total Amount (Including VAT): {allTotal_withVat}\n")

        # Printing total information
        print("--------------")
        print("TOTAL SUMMARY")
        print("--------------")
        print(f"Total Amount (Excluding VAT): {allTotal_noVat}")
        print(f"Total VAT(13%) Amount: {all_vat_amount}")
        print(f"Total Amount (Including VAT): {allTotal_withVat}")


def write_generated_return_invoice_to_file(list_of_returnable_invoices, user_info, all_total, allTotal_with_vat, all_vat_amount, all_fines, allTotal_with_fine):
    """
    Write generated return invoices to a file.

    Args:
        list_of_returnable_invoices (list): List of generated return invoices as strings.
        user_info (dict): User information including name.
        all_total (float): Total amount excluding VAT and fine.
        allTotal_with_vat (float): Total amount including VAT.
        all_vat_amount (float): Total VAT amount.
        all_fines (float): Total fine amount.
        allTotal_with_fine (float): Total amount including VAT and fine.
    """
    # Extract user name and current timestamp
    name = user_info["name"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    acceptable_timestamp = timestamp.replace(":", "_").replace(" ", "-")
    file_path = f"Invoices/return/{acceptable_timestamp}_{name}Returned.txt"
    
    with open(file_path, 'w') as file:
        for invoice in list_of_returnable_invoices:
            file.write(invoice + '\n\n')
            print(invoice + '\n\n')

    # Open the file again in append mode
    with open(file_path, 'a') as files:
        # Writing total information
        files.write("--------------\n")
        files.write("RETURN SUMMARY\n")
        files.write("--------------\n")
        files.write(f"Total Amount: {all_total}\n")
        files.write(f"Total VAT(13%) Amount: {all_vat_amount}\n")
        files.write(f"Total Amount (Including VAT): {allTotal_with_vat}\n")
        files.write(f"Total Fine: {all_fines}\n")
        files.write(f"All Total (Including VAT & Fine): {allTotal_with_fine}\n")

        # Printing total information
        print("--------------")
        print("RETURN SUMMARY")
        print("--------------")
        print(f"Total Amount: {all_total}")
        print(f"Total VAT(13%) Amount: {all_vat_amount}")
        print(f"Total Amount (Including VAT): {allTotal_with_vat}")
        print(f"Total Fine: {all_fines}")
        print(f"All Total (Including VAT & Fine): {allTotal_with_fine}")