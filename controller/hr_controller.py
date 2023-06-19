from model.hr import hr
from view import terminal as view
from model.util import generate_id
from datetime import datetime
from termcolor import colored, cprint


len_hr = {
          "len_name_hr": (2, 10),
          "len_birthday_hr": (10, 10),
          "len_department_hr": (2, 10),
          "len_nextbirthday_hr": (5, 5),
          "len_clearance_hr": (1, 2)}


len_min = 0
len_max = 1


def list_emp():
    table = hr.hr_table()[0]
    headers = hr.hr_table()[1]
    view.print_table(table, headers)
    back_from_result()


def add_emp():
    table = hr.hr_table()[0]
    print("Complete the details. If you want to quit the application, type -quit-")

    name = view.get_input("Please write a name: ")
    if name == 'quit':
        name = quit(0)
    if _is_len_correct(len(name), len_hr["len_name_hr"][len_min], len_hr["len_name_hr"][len_max]):
        view.print_message("Name correct")
    else:
        view.print_error_message(f"Invalid a employee's name, the length should be "
                         f"between {len_hr['len_name_hr'][len_min]} "
                         f"and {len_hr['len_name_hr'][len_max]}!!!")
        return add_emp()

    birth = "19999-05-13"
    while len(birth) != 10:
        birth = view.get_input("Please write an birth date: ")
        if birth == 'quit':
            birth = quit(0)
        if _is_len_correct(len(birth), len_hr["len_birthday_hr"][len_min], len_hr["len_birthday_hr"][len_max]) and _is_date_correct(birth):
            view.print_message("Birth date correct")
        else:
            view.print_error_message(f"Invalid a employee's birth, the length should be "
                         f"between {len_hr['len_birthday_hr'][len_min]} "
                         f"and {len_hr['len_birthday_hr'][len_max]}!!!")


    department = "eiwjaliwnaiwkane"
    while len(department) > 10:
        department = view.get_input("Please write a department: ")
        if department == 'quit':
            department = quit(0)
        if _is_len_correct(len(department), len_hr["len_department_hr"][len_min], len_hr["len_department_hr"][len_max]):
            view.print_message("Department correct")
        else:
            view.print_error_message(f"Invalid department, the length should be "
                        f"between {len_hr['len_department_hr'][len_min]} "
                        f"and {len_hr['len_department_hr'][len_max]}!!!")

    clearance = "abcd"
    while len(clearance) > 2:
        clearance = view.get_input("Please write a clearance: ")
        if clearance == 'quit':
            clearance = quit(0)
        if _is_len_correct(len(clearance), len_hr["len_clearance_hr"][len_min], len_hr["len_clearance_hr"][len_max]):
            view.print_message("Clearance correct")
        else:
            view.print_error_message(f"Invalid clearance, the length should be "
                f"between {len_hr['len_clearance_hr'][len_min]} "
                f"and {len_hr['len_clearance_hr'][len_max]}!!!")


    check_id = "id"
    while check_id != "":
        id = generate_id()
        check_id = hr.checking_id(table, id)
    hr.add_emp(table, id, name, birth, department, clearance)
    view.print_message(f"Employee has been succesfully added!")
    list_emp()
    back_from_result()

def update_emp():
    table = hr.hr_table()[0]
    print("Complete the details. If you want to quit the application, type -quit-")
    check_id = ""
    while check_id == "":
        id = view.get_input("Write id of employee whom you would like to update: ")
        check_id = hr.checking_id(table, id)
        if check_id == "":
            view.print_error_message("There is no employee with such id")

    name = view.get_input("Please write a name: ")
    if name == 'quit':
        name = quit(0)
    if _is_len_correct(len(name), len_hr["len_name_hr"][len_min], len_hr["len_name_hr"][len_max]):
        view.print_message("Name correct")
    else:
        view.print_error_message(f"Invalid a employee's name, the length should be "
                                     f"between {len_hr['len_name_hr'][len_min]} "
                                     f"and {len_hr['len_name_hr'][len_max]}!!!")


    birth = "19999-05-13"
    while len(birth) != 10:
        birth = view.get_input("Please write an birth date: ")
        if birth == 'quit':
            birth = quit(0)
        if _is_len_correct(len(birth), len_hr["len_birthday_hr"][len_min],
                               len_hr["len_birthday_hr"][len_max]) and _is_date_correct(birth):
            view.print_message("Birth date correct")
        else:
            view.print_error_message(f"Invalid a employee's birth, the length should be "
                                         f"between {len_hr['len_birthday_hr'][len_min]} "
                                         f"and {len_hr['len_birthday_hr'][len_max]}!!!")


    department = "eiwjaliwnaiwkane"
    while len(department) > 10:
        department = view.get_input("Please write a department: ")
        if department == 'quit':
            department = quit(0)
        if _is_len_correct(len(department), len_hr["len_department_hr"][len_min],
                               len_hr["len_department_hr"][len_max]):
            view.print_message("Department correct")
        else:
            view.print_error_message(f"Invalid department, the length should be "
                                         f"between {len_hr['len_department_hr'][len_min]} "
                                         f"and {len_hr['len_department_hr'][len_max]}!!!")


    clearance = "abcd"
    while len(clearance) > 2:
        clearance = view.get_input("Please write a clearance: ")
        if clearance == 'quit':
            clearance = quit(0)
        if _is_len_correct(len(clearance), len_hr["len_clearance_hr"][len_min],
                               len_hr["len_clearance_hr"][len_max]):
            view.print_message("Clearance correct")
        else:
            view.print_error_message(f"Invalid clearance, the length should be "
                                         f"between {len_hr['len_clearance_hr'][len_min]} "
                                         f"and {len_hr['len_clearance_hr'][len_max]}!!!")

    table = hr.updating_emp(table, id, name, birth, department, clearance)
    view.print_message(f"Employee with id {id} has been succesfully updated!")
    list_emp()
    back_from_result()

def delete_emp():
    table = hr.hr_table()[0]
    print("Complete the details. If you want to quit the application, type -quit-")
    check_id = ""
    while check_id == "":
        id = view.get_input("Write id of employee whom you would like to remove from database: ")
        check_id = hr.checking_id(table, id)
        if check_id == "":
            view.print_error_message("There is no emplyee with such id")
    table = hr.del_emp(table, id)
    hr.writing_to_file(table)
    view.print_message(f"Employee with id {id} has been succesfully removed!")
    list_emp()
    back_from_result()




def get_oldest_and_youngest():
    table = hr.hr_table()[0]
    name_youngest = hr.get_oldest_and_youngest(table)[0]
    name_oldest = hr.get_oldest_and_youngest(table)[1]
    view.print_general_results("Youngest: ", name_youngest)
    view.print_general_results("Oldest:  ", name_oldest)
    back_from_result()


def get_average_age():
    table = hr.hr_table()[0]
    date = str(datetime.now())
    now = int(date.split('-')[0])
    average = hr.get_average_age(now, table)
    view.print_general_results("Average age of employees: ", average)
    back_from_result()

def next_birthdays():
    table = hr.hr_table()[0]
    input_date = view.get_input("Please enter the date MM-DD: ")
    if input_date == 'quit':
        input_date = quit(0)
    if _is_len_correct(len(input_date), len_hr["len_nextbirthday_hr"][len_min],
                       len_hr["len_nextbirthday_hr"][len_max]) and _is_birthday_correct(input_date):
        view.print_message("Birth date correct")
    else:
        view.print_error_message(f"Invalid a employee's birth, the length should be "
                                 f"between {len_hr['len_birthday_hr'][len_min]} "
                                 f"and {len_hr['len_birthday_hr'][len_max]}!!!")
        return next_birthdays()
    output_birthday = hr.next_birthdays(input_date, table)
    view.print_general_results("Employees who have birthdays in two weeks:\t" , ",".join(x for x in output_birthday))
    back_from_result()

def count_emp_with_clearance():
    table = hr.hr_table()[0]
    lvl = view.get_input("Please enter the level of clearance: ")
    if lvl == 'quit':
        lvl = quit(0)
    if _is_len_correct(len(lvl), len_hr["len_clearance_hr"][len_min], len_hr["len_clearance_hr"][len_max]):
        view.print_message("Clearance correct")
    else:
        view.print_error_message(f"Invalid clearance, the length should be "
                                 f"between {len_hr['len_clearance_hr'][len_min]} "
                                 f"and {len_hr['len_clearance_hr'][len_max]}!!!")
        return count_emp_with_clearance()
    emp_with_clearance = hr.count_emp_with_clearance(lvl, table)
    view.print_general_results(f"Number of employees with {lvl} level: ", emp_with_clearance)
    back_from_result()




def count_emp_per_department():
    table = hr.hr_table()[0]
    dep = hr.count_emp_per_department(table)
    #.print_error_message(f"Department {dep} does not exist, please type again: ")
    #emp_in_dep = hr.count_emp_per_department(dep, table)
    view.print_general_results("The number of employees in: ", dep)
    back_from_result()




def run_operation(option):
    if option == 1:
        list_emp()
    elif option == 2:
        add_emp()
    elif option == 3:
        update_emp()
    elif option == 4:
        delete_emp()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_emp_with_clearance()
    elif option == 9:
        count_emp_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    cprint("""
                ██   ██ ██████  
                ██   ██ ██   ██ 
                ███████ ██████  
                ██   ██ ██   ██ 
                ██   ██ ██   ██ """, 'cyan', )
    cprint("\t\t\t\tSECTION", 'yellow', attrs=['bold', 'reverse'])
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    # view.clear_console()
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation\n")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)


def _is_len_correct(length, min_length, max_length):
    if min_length <= length <= max_length:
        return True
    else:
        return False


def _len_max_hr():
    len_max_list = []
    for key, value in len_hr.items():
        len_max_list.append(len_hr[key][len_max])
    return len_max_list


def _is_date_correct(date_string):
    date_format = '%Y-%m-%d'
    try:
        _ = datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False

def _is_birthday_correct(date_string):
    date_format = '%m-%d'
    try:
        _ = datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False

def back_from_result():
    menu = view.get_input("For back to HR section press enter, for quit type -quit-: \n")
    if menu == 'quit':
        view.print_message("See you later, alligator!")
        menu = quit(0)