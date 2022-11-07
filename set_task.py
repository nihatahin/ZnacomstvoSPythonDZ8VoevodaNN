#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
from valid_data import valid_role, valid_id
from records_access import append_rec_tasks, get_rec_workers, get_rec_tasks
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def print_curtask_info(task):
    print(f'\nTASK DATA.')
    print(f'Task name:\t{task[1]}')
    print(f"Task index:\t{task[0]}")
    print(f'Actuator:\t{task[2]}')
    print(f'Responsible:\t{task[3]}')
    print(f'Description:\t{task[4]}')
    print()  
#----------------------------------------------------------------------------
def set_procedure(m_id):
    valid = True
    t_name = ''
    while True:
        t_name = enter_task_name('task name', valid)
        valid = lambda valid: True if not valid else valid
        if t_name == '/return':
            return
        elif valid_role(t_name):
            break
        else:
            valid = False
    valid = True
    t_act = ''
    while True:
        t_act = enter_task_name('actor ID', valid)
        valid = lambda valid: True if not valid else valid
        if t_act == '/return':
            return
        elif valid_id(t_act) and (len(get_rec_workers()) >= int(t_act) > 0):
            break
        else:
            valid = False
    valid = True
    t_disc = ''
    while True:
        t_disc = enter_task_name('task discription', valid)
        valid = lambda valid: True if not valid else valid
        if t_disc == '/return':
            return
        else:
            break
    
    cur_task_rec = ((str(1 + len(get_rec_tasks()))), t_name, t_act, str(m_id), t_disc)
    print_curtask_info(cur_task_rec)
    valid = True
    t_act = ''
    print("Would you like to save this task ('y' - yes, 'n' - no)")
    while True:
        t_act = enter_task_name('actor ID', valid)
        valid = lambda valid: True if not valid else valid
        if (t_act == 'n') or (t_act == '/return'):
            print("Task wasn't added!")
            return
        elif t_act == 'y':
            print("Task was added!")
            append_rec_tasks(cur_task_rec)
            break
        else:
            valid = False
    

     
#----------------------------------------------------------------------------
def enter_task_name(parameter, is_valid):
    if is_valid:
        print(f'Enter {parameter}', end=' ')
    else:
        print(f"Invalid {parameter}. Please, Try again", end=' ')
    return input('(or ' + "print '/return' + Enter to return to the main menu program" + '): ')
#----------------------------------------------------------------------------
from base_func import import_full_base
from records_access import get_rec_tasks
import_success = import_full_base()
set_procedure(2)
print(get_rec_tasks())
set_procedure(1)
print(get_rec_tasks())
set_procedure(3)
print(get_rec_tasks())
from base_func import export_task
