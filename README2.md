#To Create Transactional Tables
Seperate date and time to 2 seperate colunms
Add Transactional ID
Add order ID
REMOVE Full NAme
REMOVE Card Number
#To Create Oredr Tables
Add order ID
Split orders into a line per purchase
ADD Price column changed to per purchase

**Client: From Thanks Alatte**
---
**Instructions:**
1. **Customer Privacy:** Ensure that you do not store customer names and credit card numbers in any records or databases. Maintain confidentiality and security of customer information.
2. **Payment Methods:** Retain both cash and card payment methods for transactions.
3. **Order Normalization:** Break down the list of orders into separate data entries for better reporting and analysis. Each ordered item should be recorded individually along with its price.
---
**Example:**
Original Order:
Regular Flavoured Iced Latte - Hazelnut - $2.75, Large Latte - $2.45
Normalized Orders:
1. Regular Flavoured Iced Latte - Hazelnut, $2.75
2. Large Latte, $2.45
---
**Purpose:**
The purpose of these instructions is to facilitate efficient reporting and analysis of sales data. By normalizing the order data, we can generate various reports, graphs, and visualizations to gain insights into our sales performance.
---
**Reporting Requirements:**
1. **Weekly Coffee Sales by Type:** Generate reports to determine the number of coffees sold each week and classify them by type (e.g., Regular Flavoured Iced Latte, Large Latte).
2. **Store Performance Analysis:** Compare sales figures across different stores to identify the store with the highest sales each week or day.
3. **Sales of Specific Varieties:** Calculate the total value of sales for specific coffee varieties (e.g., Hazelnut Coffee) across all stores on a weekly basis.
4. **Daily Sales of Specific Items:** Determine the total value of sales for specific items (e.g., Large Latte) across all stores on a daily basis.

**How to run files
We splite the csv files into 3 tables labelled;
Products
Orders
Transaction

-We used a try and except to connect to the database
- we used a seperate try and expect statments to create transactions table identifying the date fields of date, time ,location and transcation id (primary key), products purchased and total price and payment method
-we did the same again, creating a try and except statement for the orders table using the fields transaction id, product id, product purchased and payment method.
- finally we used another try and except to create a products table with fields product id (primary key), product and price 
- closed the connection.

*transforming data*
we imported csv file an defined our new file
-we opened and read the csv file
- created new headers
-rewrote the modified data to a new csv file
- our except statement ensure that if the file could not be found it gave an error message

- with defined a new function to remove sensitive data with a try and except of reading the intial csv file and writing a new file with the cleaned sesnsived data columns removed
-
---

If you have any questions or need further clarification, feel free to reach out.
Thank you.