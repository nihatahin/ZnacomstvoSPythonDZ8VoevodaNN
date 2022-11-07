#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
from records_access import get_rec_tasks, get_rec_workers, is_in_list, is_in_list_full
from messages import staff_msg_full
from conjoint_menu_func import enter_wrk
from valid_data import valid_id
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def task_count_for_workers(wrk, tsk):
    tsk_cnt = []
    for i in range(len(wrk)):
        cur_tsk = 0
        for j in range(len(tsk)):
            if wrk[i][0] == tsk[j][2]:
                cur_tsk += 1
        tsk_cnt.append(cur_tsk)
    return tsk_cnt
#----------------------------------------------------------------------------
def staff_list():
    workers = get_rec_workers()
    print(f"\nFull staff managees list.")
    staff_msg_full(workers, task_count_for_workers(workers, get_rec_tasks()))
#----------------------------------------------------------------------------
def empl_info():
    valid = True
    while True:
        wrk_id = enter_wrk(valid)
        valid = lambda valid: True if not valid else valid
        if wrk_id == '/return':
            break
        elif valid_id(wrk_id):
            if is_in_list(wrk_id, get_rec_workers(), 0) > 0:
                print_staff_info(is_in_list_full(wrk_id, get_rec_workers(), 0))
                break
            else:
                valid = False
        else:
            valid = False
#----------------------------------------------------------------------------
def print_staff_info(data):
    print(f'\nEMPLOYEE PERSONAL DATA.')
    print(f'Emloyee name:\t\t\t{data[1]}')
    print(f"Emloyee personal index:\t\t{data[0]}")
    print(f'Role in the company:\t\t{data[2]}')
    print(f"Tasks to do:\t\t\t{task_count_for_workers([data], get_rec_tasks())[0]}")
    print(f'Work telephone number:\t\t{data[3]}')
    print(f'Personal characteristics:\t{data[4]}')
    print()  
#----------------------------------------------------------------------------
