""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

import csv
from model import data_manager
from controller import crm_controller as control

DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]

def crm_table(): 
    table = data_manager.read_table_from_file(DATAFILE)
    return table, HEADERS

def adding_customer(table, id, name, email,subscribe):
    new_record = []
    new_record.append(id)
    new_record.append(name)
    new_record.append(email)
    new_record.append(subscribe)
    table.append(new_record)
    writing_to_file(table)
    return table

def deleting_customer(table, id):
    for i in table:
        if i[0] == id:
            table.remove(i)
    return table

def writing_to_file(table):
    data_manager.write_table_to_file(DATAFILE, table)

def print_subscribed(table):
    subscribed = [i[2] for i in table if i[3] == '1']
    return ", ".join(subscribed)

def updating_customer(table, id, name, email, subscribe):
    for i in table:
        if i[0] == id:
            id = i[0]
            i[1] = name
            i[2] = email
            i[3] = subscribe
    writing_to_file(table)
    return table

def checking_id(table, id):
    id_check = ""
    for i in table:
        if i[0] == id:
            id_check = i[0]
    return id_check