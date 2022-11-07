#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
from records_access import get_rec_len
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def welcome_print(name):
    print(f"Welcome, {name}! We are glad to see you!")
#----------------------------------------------------------------------------
def file_start_work(path):
    with open (path, 'r', encoding= 'utf-8') as help_file:
        print(help_file.read())
#----------------------------------------------------------------------------
def exit_print():
    print('You leave WorkBUG profile!')
#----------------------------------------------------------------------------
def enter_cmd(is_valid):
    if is_valid:
        print('Enter command', end='')
    else:
        print('Invalid command was entered. Please, Try again', end='')
    return input(': ')
#----------------------------------------------------------------------------
def is_worker_len(record):
    return len(record) == get_rec_len('wrk')
#---------------------------------------------------------------------------
def enter_tsk(is_valid):
    if is_valid:
        print('Enter task ID', end=' ')
    else:
        print(f"You haven't got task with this ID. Please, Try again", end=' ')
    return input('(or ' + "print '/return' + Enter to return to the main menu program" + '): ')
#----------------------------------------------------------------------------
def enter_wrk(is_valid):
    if is_valid:
        print('Enter employee ID', end=' ')
    else:
        print(f"There isn't such ID in data base. Please, Try again", end=' ')
    return input('(or ' + "print '/return' + Enter to return to the main menu program" + '): ')
#----------------------------------------------------------------------------