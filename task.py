#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
from conjoint_menu_func import is_worker_len
from messages import task_msg_full
from records_access import get_rec_tasks
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
