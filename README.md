# SecureERP

SecureERP is an enterprise resource planning (ERP) software developed for a client who prioritizes security and offline functionality. The client requested a short and clean codebase that works strictly on local files, ensuring data privacy and minimizing exposure to online threats.

## Project Overview

The goal of SecureERP is to provide a highly modular structure that separates code for different content areas while enforcing a single channel for user interactions and file input/output operations. The project follows a variant of the Model-View-Controller (MVC) architecture specifically designed for a terminal-based application that works with local data files.

### CRM Module

The CRM module in SecureERP focuses on customer relationship management. It provides basic and special operations to manage customer data.

1. **Create a New Customer**: When selecting this option, the user can input the name, email, and subscription status for a new customer. A unique ID is automatically assigned to the customer.

2. **Print All Customers**: This option allows users to view the details of all existing customers.

3. **Update Customer Details**: Users can update the name, email, and subscription status for a specific customer by entering the customer's ID.

4. **Delete Customer**: Users can delete a customer from the database by providing the customer's ID.

5. **Get Subscribed Customer Emails**: This option retrieves the emails of all subscribed customers.

### Sales Module

The Sales module in SecureERP handles sales-related operations. It includes basic and special functionalities.

1. **Create, Read, Update, Delete (CRUD) Operations**: Users can perform basic CRUD operations on sales transactions.

2. **Get Transaction with the Highest Revenue**: This option retrieves the details of the transaction that generated the highest revenue.

3. **Get Product with the Highest Overall Revenue**: Users can obtain information about the product that generated the highest revenue overall.

4. **Count Transactions between Two Dates**: Users can count the number of transactions that occurred within a specified date range.

5. **Sum of Transaction Prices between Two Dates**: This option calculates the total price of transactions that occurred between two specified dates.

### HR Module

The HR module in SecureERP handles human resources-related operations. It includes basic and special functionalities.

1. **CRUD Operations**: Users can perform basic CRUD operations on employee data.

2. **Get Oldest and Youngest Employees**: This option returns the names of the oldest and youngest employees as a tuple.

3. **Get Average Employee Age**: Users can obtain the average age of all employees.

4. **Get Employees with Upcoming Birthdays**: This option returns the names of employees whose birthdays fall within two weeks from the input date.

5. **Count Employees with Clearance Level**: Users can retrieve the number of employees who have at least the specified clearance level.

6. **Count Employees per Department**: This option returns the number of employees per department in the form of a dictionary.

## Installation

To set up and run SecureERP, follow these steps:

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required dependencies.
4. Run the SecureERP application with main file.

Follow the on-screen instructions to navigate and interact with the different modules of SecureERP.

## Contributing

Contributions to SecureERP are welcome! If you have any bug fixes, enhancements, or new features to propose, please feel free to submit a pull request. Ensure that your code follows the project's coding conventions and includes relevant tests.
