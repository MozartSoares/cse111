#to exceed the requirements i've added a formatted receipt, i've also added the "return by" line to the receipt

import csv
from datetime import datetime, timedelta
from pprint import pprint

def read_dictionary(filepath,key_column_index=0):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    try:
        with open(filepath,'r') as file:
            reader = csv.reader(file)
            next(reader)
            dictionary = {}
            
            for row in reader:
                if len(row) != 0 : 
                    key = row[key_column_index]
                    dictionary[key] = row
        return dictionary
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
        return {}
    except PermissionError:
        print(f"Error: You do not have permission to read the file {filepath}.")
        return {}


def main():
    requests_filename = 'request.csv'
    store_name = "Mozart's Grocery Store"
    tax_rate = 0.06
    
    products_dict = read_dictionary('products.csv',0)
    if (not products_dict):
        return
    
    total_items = 0
    subtotal = 0
    
    try:
        with open(requests_filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  
            
            try: 
                print(f"<----{store_name}---->\n")
                print("Item Name      Quantity    Unit Price    Total Price")
                print("--------------------------------------------------")

                for row in reader:
                    if len(row) != 0:
                        product_key = row[0]
                        quantity = int(row[1])
                        product = products_dict[product_key]
                        product_name = product[1]  
                        product_price = float(product[2]) 
                            
                        total_price = product_price * quantity
                        total_items += quantity
                        subtotal += total_price
                            
                        print(f"{product_name:<15} {quantity:<10} {product_price:<12.2f} {total_price:.2f}")
                        
            except KeyError:
                print(f"Error: unknown product ID in {requests_filename}: {product_key}")
                return 
            
            sales_tax = subtotal * tax_rate
            total = subtotal + sales_tax
            current_datetime = datetime.now().strftime("%a %b %d %H:%M:%S %Y")  
            return_by_date = datetime.now() + timedelta(days=30)
            return_by_date = return_by_date.replace(hour=21, minute=0, second=0, microsecond=0)
            return_by_str = return_by_date.strftime("%a %b %d %H:%M:%S %Y")   
            
            print("\n--------------------------------------------------")
            print(f"Total Items: {total_items}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Sales Tax (6%): ${sales_tax:.2f}")
            print(f"Total: ${total:.2f}")
            
            print("\nThank you for shopping with us!\n")
            print(f"Date/Time: {current_datetime}")
            
            print(f"Return by: {return_by_str}")
    
    except FileNotFoundError:
        print("Error: The file 'request.csv' was not found.")
    except PermissionError:
        print("Error: You do not have permission to read 'request.csv'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == '__main__':
    main()