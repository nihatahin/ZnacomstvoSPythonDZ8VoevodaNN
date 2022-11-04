#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
from records_access import get_rec_managers, is_in_list_full
from conjoint_menu_func import exit_print, welcome_print, file_start_work, enter_cmd
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------
help_path = './files/help_mng.txt'
#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def personal_data_mng(id_m):
    return is_in_list_full(str(id_m), get_rec_managers(), 0)
#----------------------------------------------------------------------------
def get_help_path():
    return help_path
#----------------------------------------------------------------------------
def mng_menu(id):
    manager_data = personal_data_mng(id)
    welcome_print(manager_data[1])
    file_start_work(get_help_path())
    basement()
#----------------------------------------------------------------------------
def basement():
    valid = True
    while True:
        cmd = enter_cmd(valid)
        valid = lambda valid: True if not valid else valid
        match cmd:
            case '/info':
                print("Info") 
            case '/mytask':
                print("Tasks")
            case '/staff':
                print("Staff")
            case '/worker':
                print("Worker")
            case '/taskinfo':
                print("Infotask") 
            case '/closetask':
                print("Close")
            case '/settask':
                print("Set")
            case '/return':
                exit_print()
                break
            case _:
                valid= False