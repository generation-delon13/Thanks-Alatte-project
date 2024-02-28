import csv
# creates new transaction csv with headers 
def create_new_csv(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            reader = csv.reader(file)
            transaction_data = list(reader)
            
            # Header
            header = ['Date & Time', 'Location', 'Full Name', 'Products Purchased & Price', 'Total Price', 'Payment Method', 'Card Number']
            
            
            with open(output_file, 'w', newline='') as new_file:
                csv_writer = csv.writer(new_file)
                csv_writer.writerow(header)  

                
                for row in transaction_data:
                    date_time = row[0]
                    location = row[1]
                    full_name = row[2]
                    products_and_prices = row[3]
                    total_price = row[4]
                    payment_method = row[5]
                    card_number = row[6]
                    
                
                    # Write the modified data to the new file
                    csv_writer.writerow([date_time, location, full_name, products_and_prices, total_price, payment_method, card_number])

        print(f"Transformation completed. New file: {output_file}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
create_new_csv('transactions.csv', 'new_transactions.csv')
# removes sensitive data for csv file
def remove_sensitive_data(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            reader = csv.reader(file)
            transaction_data = list(reader)
            
            # Header
            header = ['Date & Time', 'Location', 'Products Purchased & Price', 'Payment Method']
            
            
            with open(output_file, 'w', newline='') as new_file:
                csv_writer = csv.writer(new_file)
                csv_writer.writerow(header)  # Write the new header to the new file

                
                for row in transaction_data:
                    date_time = row[0]
                    location = row[1]
                    products_and_prices = row[3]
                    total_price = row[4]
                    payment_method = row[5]
                    
                    # Write the modified data to the new file
                    csv_writer.writerow([date_time, location, products_and_prices, total_price, payment_method])

        print(f"Transformation completed. New file: {output_file}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
remove_sensitive_data('transactions.csv', 'new_transactions.csv')