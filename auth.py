#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
from records_access import get_rec_workers, get_rec_managers, is_in_list, name_and_role_prepare
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def enter_nm(is_valid):
    if is_valid:
        print('Enter your name', end=' ')
    else:
        print("Entered name lackes in data base. Enter new one", end=' ')
    return input('(or ' + "print '/exit' + Enter to exit program" + '): ')
#----------------------------------------------------------------------------
def exit_func():
    print("You leave WorkBUG. It is a pity!")
#----------------------------------------------------------------------------
def wrk_search(name):
    return is_in_list(name_and_role_prepare(name), get_rec_workers(), 1)
#----------------------------------------------------------------------------
def mng_search(name):
    return is_in_list(name_and_role_prepare(name), get_rec_managers(), 1)
#----------------------------------------------------------------------------
def auth_logic():
    valid = True
    while True:
        name = enter_nm(valid)
        valid = lambda valid: True if not valid else valid
        cur_id = wrk_search(name)
        if cur_id > 0:
            print(f"Worker #{cur_id}!")
        else:
            cur_id = mng_search(name)
            if cur_id > 0:
                print(f"Manager #{cur_id}!")
            elif name == '/exit':
                exit_func()
                return
            else:
                valid = False