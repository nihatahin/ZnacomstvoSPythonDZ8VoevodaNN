#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
from records_access import get_rec_workers, is_in_list_full
from conjoint_menu_func import exit_print, welcome_print, file_start_work, enter_cmd
from info_cmd import print_info
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------
help_path = './files/help_wrk.txt'
#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def personal_data_wrk(id_w):
    return is_in_list_full(str(id_w), get_rec_workers(), 0)
#----------------------------------------------------------------------------
def get_help_path():
    return help_path
#----------------------------------------------------------------------------
def wrk_menu(id):
    worker_data = personal_data_wrk(id)
    welcome_print(worker_data[1])
    file_start_work(get_help_path())
    basement(worker_data)
#----------------------------------------------------------------------------
def basement(w_data):
    valid = True
    while True:
        cmd = enter_cmd(valid)
        valid = lambda valid: True if not valid else valid
        match cmd:
            case '/info':
                print_info(w_data)
            case '/mytask':
                print("Tasks") 
            case '/taskinfo':
                print("Infotask") 
            case '/closetask':
                print("Close") 
            case '/return':
                exit_print()
                break
            case _:
                valid= False