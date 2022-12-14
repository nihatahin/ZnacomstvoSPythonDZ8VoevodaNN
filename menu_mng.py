#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
from records_access import get_rec_managers, is_in_list_full
from conjoint_menu_func import exit_print, welcome_print, file_start_work, enter_cmd
from info_cmd import print_info
from task import personal_task_list, task_info, close_task
from staff import staff_list, empl_info
from set_task import set_procedure
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
    basement(manager_data)
#----------------------------------------------------------------------------
def basement(m_data):
    valid = True
    while True:
        file_start_work(get_help_path())
        cmd = enter_cmd(valid)
        valid = lambda valid: True if not valid else valid
        match cmd:
            case '/info':
                print_info(m_data) 
            case '/mytask':
                personal_task_list(m_data) 
            case '/staff':
                staff_list()
            case '/worker':
                empl_info()
            case '/taskinfo':
                task_info(m_data)
            case '/closetask':
                close_task(m_data)
            case '/settask':
                set_procedure(m_data[0])
            case '/return':
                exit_print()
                break
            case _:
                valid= False