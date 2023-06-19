""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

import csv
#from datetime import datetime, timedelta
import datetime

from model import data_manager, util
#from controller import hr_controller as control

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def hr_table():
    table = data_manager.read_table_from_file(DATAFILE)
    return table, HEADERS


def writing_to_file(table):
    data_manager.write_table_to_file(DATAFILE, table)


def add_emp(table, id, name, birth, department, clearance):
    new_record = []
    new_record.append(id)
    new_record.append(name)
    new_record.append(birth)
    new_record.append(department)
    new_record.append(clearance)
    table.append(new_record)
    writing_to_file(table)
    return table


def del_emp(table, id):
    for i in table:
        if i[0] == id:
            table.remove(i)
    return table


def updating_emp(table, id, name, birth, department, clearance):
    for i in table:
        if i[0] == id:
            id = i[0]
            i[1] = name
            i[2] = birth
            i[3] = department
            i[4] = clearance
    writing_to_file(table)
    return table


def checking_id(table, id):
    id_check = ""
    for i in table:
        if i[0] == id:
            id_check = i[0]
    return id_check


def get_oldest_and_youngest(table):
    birth_date_oldest = datetime.datetime(2001,6,22)
    name_oldest = ""
    birth_date_youngest = datetime.datetime(1980, 6, 22)
    name_youngest = ""
    for i in table:
        date = i[2].split('-')
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
        date = datetime.datetime(year,month,day)
        if date < birth_date_oldest:
            birth_date_oldest = date
            name_oldest = i[1]
        if date > birth_date_youngest:
            birth_date_youngest = date
            name_youngest = i[1]
    return name_youngest, name_oldest


def get_average_age(now, table):
    sume = 0
    for i in table:
        date = i[2].split('-')
        year = int(date[0])
        sume += now - year
    average = sume // len(table)
    return average


def next_birthdays(input_date, table):
    list_name = []
    input_date = input_date.split('-')
    year = 2022
    month = int(input_date[0])
    day = int(input_date[1])
    input_date = datetime.datetime(year, month, day)
    for i in table:
        date = i[2].split('-')
        year = 2022
        month = int(date[1])
        day = int(date[2])
        date = datetime.datetime(year, month, day)
        if (date - input_date).days <= 14:
            list_name.append(i[1])
    return list_name


def count_emp_with_clearance(lvl, table):
    elements = []
    lvl_int = int(lvl)
    for i in table:
        clearance = int(i[4])
        if lvl_int <= clearance:
            elements.append(i[4])
    number_of_emp = len(elements)
    return number_of_emp


def count_emp_per_department(table):
    emp_in_dep = {}
    for i in table:
        if i[3] in emp_in_dep:
            emp_in_dep[i[3]] += 1
        else:
            emp_in_dep[i[3]] = 1
    return emp_in_dep







