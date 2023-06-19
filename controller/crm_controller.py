import csv
from view import terminal as view
import sys
import os
from model.crm import crm
from model.util import generate_id
from termcolor import colored, cprint





def list_customers():
    table = crm.crm_table()[0]
    headers = crm.crm_table()[1]
    view.print_table(table, headers)
    back_from_result()


def add_customer():
    subscribe = None
    table = crm.crm_table()[0]
    name = view.get_input("Please write a name: ")
    email = view.get_input("Please write an e-mail: ")
    while subscribe != '0' and subscribe != '1':
        subscribe = str(view.get_input("Write '1' if you want to subscribe or '0' if not: "))
    check_id = "id"
    while check_id != "":
        id = generate_id()
        check_id = crm.checking_id(table, id)
    crm.adding_customer(table, id, name, email, subscribe)
    view.print_message(f"Customer has been succesfully added!")
    list_customers()
    back_from_result()

def update_customer():
    table = crm.crm_table()[0]
    subscribe = None
    check_id = ""
    while check_id == "":
        id = view.get_input("Write id of customer whom you would like to update: ")
        check_id = crm.checking_id(table, id)
        if check_id == "":
            view.print_error_message("There is no customer with such id")
    name = view.get_input("Write a new name: ")
    email = view.get_input("Write a new e-mail: ")
    while subscribe != '0' and subscribe != '1':
        subscribe = str(view.get_input("Write '1' if you want to subscribe or '0' if not: "))
    table = crm.updating_customer(table, id, name, email, subscribe)
    view.print_message(f"Customer with id {id} has been succesfully updated!")
    list_customers()
    back_from_result()


def delete_customer():
    table = crm.crm_table()[0]
    check_id = ""
    while check_id == "":
        id = view.get_input("Write id of customer whom you would like to remove from database: ")
        check_id = crm.checking_id(table, id)
        if check_id == "":
            view.print_error_message("There is no customer with such id")
    table = crm.deleting_customer(table, id)
    crm.writing_to_file(table)
    view.print_message(f"Customer with id {id} has been succesfully removed!")
    list_customers()
    back_from_result()

def get_subscribed_emails():
    table = crm.crm_table()[0]
    subscribed = crm.print_subscribed(table)
    view.print_general_results("Subscribed customer emails: ", subscribed)
    back_from_result()



def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    cprint("""
             ██████ ██████  ███    ███ 
            ██      ██   ██ ████  ████ 
            ██      ██████  ██ ████ ██ 
            ██      ██   ██ ██  ██  ██ 
             ██████ ██   ██ ██      ██  """, 'cyan', )
    cprint("\t\t\tSECTION", 'yellow', attrs=['bold', 'reverse'])
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)


def back_from_result():
    menu = view.get_input("For back to HR section press enter, for quit type -quit-: \n")
    if menu == 'quit':
        view.print_message("See you later, alligator!")
        menu = quit(0)