""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from controller import sales_controller as control
from model import data_manager
from model import util

import datetime, csv
from random import randint, random



DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]


def sales_table():
    """ Open file and read sales.csv"""
    table = data_manager.read_table_from_file(DATAFILE)
    return table, HEADERS

#----------------------------------------------------------

def writing_to_file(table):
    """ Write database to file"""
    data_manager.write_table_to_file(DATAFILE, table)

#----------------------------------------------------------------

def data_table(list):
    """ create dictionary and write it to the list"""
    data_structur = {}
    list_table = []
    lenght = len(list)
    for i in range(lenght):
        temp = list[i]
        data_structur = {
            'id': temp[0],
            'customer': temp[1],
            'product': temp[2],
            'price': temp[3],
            'date' : temp[4],
        }
        list_table.append(data_structur)
    return list_table

#--------------------------------------------------------------------

def add_transacion(table, id, customer_id, product, price, date):
    """ adding new record to database """
    new_record = []
    new_record.append(id)
    new_record.append(customer_id)
    new_record.append(product)
    new_record.append(price)
    new_record.append(date)
    table.append(new_record)
    return table


#-----------------------------------------------------------------------------------------

def updating_transacion(table, id, customer_id, product, price, date):
    for i in table:
        if i[0] == id:
            id = i[0]
            i[1] = customer_id
            i[2] = product
            i[3] = price
            i[4] = date
    return table

#-----------------------------------------------------------------------------------

def del_transacion(table, id):
    """ delete record"""
    for i in table:
        if i[0] == id:
            table.remove(i)
    return table

#--------------------------------------------------------------------------------------------

def biggest_revenue_transaction() -> float:
    """ The function return ID of transaction that made the biggest revenue. """

    data_base = sales_table()
    revenue_list = []
    biggest_transaction = 0

    for i in range(len(data_base)):
        revenue_list.append(float(data_base[i][3]))
        if float(data_base[i][3]) == max(revenue_list):
            biggest_transaction = data_base[i][0]
    return biggest_transaction


def product_with_biggest_revenue() -> str:
    """ The function return product that made the biggest revenue altogether. """

    data_base = sales_table()
    products_revenue = {}
    product = ""

    for i in range(len(data_base)):
        if data_base[i][2] in products_revenue:
            products_revenue[data_base[i][2]] += float(data_base[i][3])
        else:
            products_revenue[data_base[i][2]] = float(data_base[i][3])
            product = max(products_revenue, key=products_revenue.get)
    return product


def get_transactions_between(start_date: str, end_date: str) -> list:
    """ The function count the number of transactions between two dates. """

    data_base = sales_table()
    transaction_list = []
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    for i in range(len(data_base)):
        date = data_base[i][4]
        date = datetime.strptime(date, '%Y-%m-%d')
        if start_date <= date <= end_date:
            transaction_list.append(data_base[i])
    return transaction_list


def number_of_transactions_between(start_date: str, end_date: str) -> int:
    """ The function count the number of transactions between two dates. """

    return len(get_transactions_between(start_date, end_date))


def sum_of_transactions_prices_between(start_date: str, end_date: str) -> float:
    """ The function count the price of transactions between two dates. """

    transaction_list = get_transactions_between(start_date, end_date)
    sum_of_transactions_prices = 0

    for i in transaction_list:
        sum_of_transactions_prices += float(i[3])
        sum_of_transactions_prices = round(sum_of_transactions_prices, 2)
    return sum_of_transactions_prices

def checking_id(table, id):
    id_check = ""
    for i in table:
        if i[0] == id:
            id_check = i[0]
    return id_check