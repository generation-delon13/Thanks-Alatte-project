import boto3
import csv
import io

s3 = boto3.client('s3')
# transaction table
def create_transactions(input_data):
    output_data = []
    header = ['Date', 'Time', 'Location', 'Products Purchased', 'Total Price', 'Payment Method']

    for row in input_data:
        date_time = row[0]
        location = row[1]
        products_and_prices = row[3]
        total_price = row[4]
        payment_method = row[5]

        date, time = date_time.split(' ')

        products_purchased_cleaned = ', '.join([item.split('-')[0].strip() for item in products_and_prices.split(',')])

        output_data.append([date, time, location, products_purchased_cleaned, total_price, payment_method])

    return output_data    
def lambda_handler(event, context):
    bucket_name = 'thanksalatte-raw-bucket'
    clean_bucket = 'thanksalatte-bucket'
    original_file_name = 'transactions.csv'
    new_file_name = 'clean-transactions.csv' 

    try:
        response = s3.get_object(Bucket=bucket_name, Key=original_file_name)
        transaction_data = list(csv.reader(io.StringIO(response['Body'].read().decode('utf-8'))))
        
        transformed_data = create_transactions(transaction_data)
    
        csv_buffer = io.StringIO()
        csv_writer = csv.writer(csv_buffer)
        csv_writer.writerows(transformed_data)
        s3.put_object(Bucket=clean_bucket, Key=new_file_name, Body=csv_buffer.getvalue(), ContentType='text/csv')

        return {
            'statusCode': 200,
            'body': f'Modified CSV saved as {new_file_name} in S3 bucket'
        }
    except Exception as e:
        error_message = f"Error processing or uploading CSV file: {str(e)}"