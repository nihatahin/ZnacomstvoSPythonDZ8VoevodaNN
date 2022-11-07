#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
from conjoint_menu_func import is_worker_len, enter_tsk
from messages import task_msg_full
from records_access import get_rec_tasks, is_in_list_full, get_rec_managers, get_rec_workers, del_rec_task, modify_task
from valid_data import valid_id
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def my_tasks(my_id, col):
    full_tasks = get_rec_tasks()
    task_my  = []
    for i in range(len(full_tasks)):
        if my_id == full_tasks[i][col]:
            task_my.append(full_tasks[i])
    return task_my
#----------------------------------------------------------------------------
def personal_task_list(data):
    col_num = 2 if is_worker_len(data) else 3
    print(f"\nTask list that {'has been set to you' if col_num == 2 else 'you have set'}.")
    my_task_list = my_tasks(data[0], col_num)
    task_msg_full(my_task_list)
#----------------------------------------------------------------------------
def task_in_list(task, id, col):
    full_tasks = get_rec_tasks()
    for i in range(len(full_tasks)):
        if (task == full_tasks[i][0]) and (id == full_tasks[i][col]):
            return True
    return False
#----------------------------------------------------------------------------
def task_info(data):
    col_num = 2 if is_worker_len(data) else 3
    valid = True
    while True:
        tsk = enter_tsk(valid)
        valid = lambda valid: True if not valid else valid
        if tsk == '/return':
            break
        elif valid_id(tsk):
            if task_in_list(tsk, data[0], col_num):
                print_task_info(tsk)
                break
            else:
                valid = False
        else:
            valid = False
#----------------------------------------------------------------------------
def print_task_info(task_id):
    task = is_in_list_full(task_id, get_rec_tasks(), 0)
    print(f'\nTASK DATA.')
    print(f'Task name:\t{task[1]}')
    print(f"Task index:\t{task[0]}")
    print(f'Actuator:\t{is_in_list_full(task[2], get_rec_workers(), 0)[1]}')
    print(f'Responsible:\t{is_in_list_full(task[3], get_rec_managers(), 0)[1]}')
    print(f'Description:\t{task[4]}')
    print()
#----------------------------------------------------------------------------
def close_task(data):
    col_num = 2 if is_worker_len(data) else 3
    valid = True
    while True:
        tsk = enter_tsk(valid)
        valid = lambda valid: True if not valid else valid
        if tsk == '/return':
            break
        elif valid_id(tsk):
            if task_in_list(tsk, data[0], col_num):
                del_task(tsk)
                break
            else:
                valid = False
        else:
            valid = False
#----------------------------------------------------------------------------
def del_task(task):
    t_i = int(task)
    del_rec_task(t_i - 1)
    t_list = get_rec_tasks()
    for i in range(len(t_list)):
        cut_t_i = int(t_list[i][0])
        if cut_t_i > t_i:
            modify_task(i, 0, str(cut_t_i - 1)) 
    print("Task was deleted from database.")
#----------------------------------------------------------------------------