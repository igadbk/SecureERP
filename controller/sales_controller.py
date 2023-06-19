from numpy import product
from controller.crm_controller import back_from_result
from model.sales import sales
from view import terminal as view
from model.sales import util as util
from termcolor import colored, cprint


def list_transactions():
    table = sales.sales_table()[0]
    headers = sales.sales_table()[1]
    view.print_table(table, headers)
    back_from_result()

#-----------------------------------------------------------------

def add_transaction():
    """ add new transacion to database """
    customer_id = util.generate_id
    table = sales.sales_table()[0]
    customer_id = util.generate_id() 
    product = view.get_input("Please write a product name: ")
    while True:
        price = view.get_input("Please write an product price : ")
        if price.isalpha == True:
            print("Only digits! ")
            continue
        else:
            price = float(price)
            break  
    check_id = "id"
    while check_id != "":
        id = util.generate_id()
        check_id = sales.checking_id(table, id)
    date = "19999-05-13"
    while len(date) != 10:
        date = view.get_input("Please write a date: ")
        if date == 'quit':
            date = quit(0)
    sales.add_transacion(table, id, customer_id, product, price, date)
    sales.writing_to_file(table)
    view.print_message(f"\nTransaction have been added to the list.")
    list_transactions()   
    view.getch()
    view.screenClean()
    back_from_result() 

#---------------------------------------------------------------------------------

def update_transaction():
    table = sales.sales_table()[0]
    check_id = ""
    while check_id == "":
        id = view.get_input("Write id of transacion which you would like to update: ")
        check_id = sales.checking_id(table, id)
        if check_id == "":
            view.print_error_message("There is no transacion with such id")
    product = view.get_input("Write a new product name: ")
    customer_id = view.get_input("Write a new customer_id: ")
    while True:
        price = view.get_input("Please write an new price : ")
        if price.isalpha == True:
            print("Only digits! ")
            continue
        else:
            price = float(price)
            break
    while len(date) != 10:
        date = view.get_input("Please write a date: ")
        if date == 'quit':
            date = quit(0)  
    table = sales.add_transacion(table, id, customer_id, product, price, date)
    sales.writing_to_file(table)
    view.print_message(f"Transacion with id {id} has been succesfully updated!")
    list_transactions()
    sales.updating_transacion()
    view.getch()
    view.screenClean()
    back_from_result()

#-----------------------------------------------------------------------------------

def delete_transaction():
    table = sales.sales_table()[0]
    check_id = ""
    while check_id == "":
        id = view.get_input("Write id of transacion whichh you would like to remove from database: ")
        check_id = sales.checking_id(table, id)
        if check_id == "":
            view.print_error_message("There is no customer with such id")
    table = sales.del_transacion(table, id)
    sales.writing_to_file(table)
    view.print_message(f"Customer with id {id} has been succesfully removed!")
    sales.del_transacion()
    view.getch()
    view.screenClean()
    back_from_result

#----------------------------------------------------------------------------------

def get_biggest_revenue_transaction():
    biggest_transaction = sales.biggest_revenue_transaction()
    view.print_message("\nID of transaction that made the biggest revenue: ")
    view.print_biggest_revenue_transaction(biggest_transaction)
    view.print_message("")
    view.getch()
    view.screenClean()

#------------------------------------------------------------------------------------

def get_biggest_revenue_product():
    product = sales.product_with_biggest_revenue()
    view.print_message("\nProduct that made the biggest revenue altogether: ")
    view.print_product_with_biggest_revenue(product)
    view.print_message("")
    view.getch()
    view.screenClean()

#---------------------------------------------------------------------------------

def count_transactions_between():
    start_date = view.get_input("Please enter start date (YYYY-MM-DD): ")
    end_date = view.get_input("Please enter end date (YYYY-MM-DD): ")
    if view.correct_date(start_date) and view.correct_date(end_date):
        number_of_transaction = sales.number_of_transactions_between(start_date, end_date)
        view.print_message("\nNumber of transactions between two dates: ")
        view.print_number_of_transactions_between(number_of_transaction)
        view.print_message("")
        view.getch()
        view.screenClean()
    else:
        view.print_error_message("Wrong dates. Pleas enter correct ones.")
        view.getch()
        view.screenClean()

#-------------------------------------------------------------------------------------

def sum_transactions_between():
    start_date = view.get_input("Please enter start date (YYYY-MM-DD): ")
    end_date = view.get_input("Please enter end date (YYYY-MM-DD): ")
    if view.correct_date(start_date) and view.correct_date(end_date):
        sum_of_transactions_prices = sales.sum_of_transactions_prices_between(start_date, end_date)
        view.print_message("\nSum of transactions prices between two dates: ")
        view.print_sum_of_transactions_prices_between(sum_of_transactions_prices)
        view.print_message("")
        view.getch()
        view.screenClean()
    else:
        view.print_error_message("Wrong dates. Pleas enter correct ones.")
        view.getch()
        view.screenClean()

#--------------------------------------------------------------------------------------

def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")

#--------------------------------------------------------------------------------

def display_menu():
    view.screenClean()
    cprint("""
                ███████  █████  ██      ███████ ███████ 
                ██      ██   ██ ██      ██      ██      
                ███████ ███████ ██      █████   ███████ 
                     ██ ██   ██ ██      ██           ██ 
                ███████ ██   ██ ███████ ███████ ███████ """, 'cyan', )
    cprint("\t\t\t\tSECTION", 'yellow', attrs=['bold', 'reverse'])
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)

#---------------------------------------------------------------------------------

def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)

#-----------------------------------------------------------------------------------

def back_from_result():
    menu = view.get_input("For back to Sales section press enter, for quit type -quit-: \n")
    if menu == 'quit':
        view.print_message("See you later, alligator!")
        menu = quit(0)