#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
from valid_data import valid_id, valid_name, valid_role, valid_phone
from records_access import append_rec_managers, append_rec_tasks, append_rec_workers, get_rec_tasks
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------
managers_path = './files/base/managers.md'
workers_path = './files/base/workers.md'
tasks_path = './files/base/tasks.md'
#----------
top_head = \
    {
        'm' : ('|manager_id|Name|Role|Telephone number|\n', '|-:|-:|-:|-:|\n'),
        'w' : ('|worker_id|Name|Role|Telephone number|Characteristics|\n', '|-:|-:|-:|-:|:-|\n'),
        't' : ('|task_id|Name|worker_id|manager_id|Description|\n', '|-:|-:|-:|-:|:-|\n')
    }
column_num = \
    {
        'm' : 4,
        'w' : 5,
        't' : 5
    }
#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def get_managers_path():
    return managers_path
#----------------------------------------------------------------------------
def get_workers_path():
    return workers_path
#----------------------------------------------------------------------------
def get_tasks_path():
    return tasks_path
#----------------------------------------------------------------------------
def get_top_head():
    return top_head
#----------------------------------------------------------------------------
def get_column_num():
    return column_num
#----------------------------------------------------------------------------
def import_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines
#----------------------------------------------------------------------------
def top_head_check(key, tpl):
    return tpl == get_top_head()[key]
#----------------------------------------------------------------------------
def split_line_data(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].split('|')
    return lines
#----------------------------------------------------------------------------
def column_num_check(recs, k):
    for i in range(len(recs)):
        if (len(recs[i]) - 2) != get_column_num()[k]:
            return False
    else:
        return True
#----------------------------------------------------------------------------
def delete_unnec_elements(recs):
    for i in range(len(recs)):
        recs[i] = recs[i][1 : -1]
    else:
        return recs
#----------------------------------------------------------------------------
def id_check(records):
    for i in range(len(records)):
        if int(records[i][0]) != i + 1:
            return False
    else:
        return True
#----------------------------------------------------------------------------
def content_check_workers(records):
    for i in range(len(records)):
        if not(valid_id(records[i][0])):
            return False
        if not(valid_name(records[i][1])):
            return False
        if not(valid_role(records[i][2])):
            return False
        if not(valid_phone(records[i][3])):
            return False
    else:
        return True
#----------------------------------------------------------------------------
def content_check_managers(records):
    for i in range(len(records)):
        if not(valid_id(records[i][0])):
            return False
        if not(valid_name(records[i][1])):
            return False
        if not(valid_role(records[i][2])):
            return False
        if not(valid_phone(records[i][3])):
            return False
    else:
        return True
#----------------------------------------------------------------------------
def content_check_tasks(records):
    for i in range(len(records)):
        if not(valid_id(records[i][0])):
            return False
        if not(valid_role(records[i][1])):
            return False
        if not(valid_id(records[i][2])):
            return False
        if not(valid_id(records[i][3])):
            return False
    else:
        return True
#----------------------------------------------------------------------------
def content_check(recs, key):
    match key:
        case 'w':
            return content_check_workers(recs)
        case 'm':
            return content_check_managers(recs)
        case 't':
            return content_check_tasks(recs)
        case _:
            return False
#----------------------------------------------------------------------------
def content_append(recs, key):
    match key:
        case 'w':
            for i in range(len(recs)):
                append_rec_workers(recs[i])
        case 'm':
            for i in range(len(recs)):
                append_rec_managers(recs[i])
        case 't':
            for i in range(len(recs)):
                append_rec_tasks(recs[i])
        case _:
            return False
#----------------------------------------------------------------------------
def import_full_base():
    return import_one_table(get_workers_path(), 'w') and import_one_table(get_managers_path(), 'm') and import_one_table(get_tasks_path(), 't')
#----------------------------------------------------------------------------
def import_one_table(path, key):
    data = import_file(path)
    if top_head_check(key, tuple(data[: 2])):
        data = split_line_data(data[2 : ])
        if column_num_check(data, key):
            data = delete_unnec_elements(data)
            if content_check(data, key):  
                if id_check(data):
                    content_append(data, key)
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
#----------------------------------------------------------------------------
def export_task():
    with open(get_tasks_path(), 'w', encoding='utf-8') as file:
        file.write('|task_id|Name|worker_id|manager_id|Description|\n|-:|-:|-:|-:|:-|\n')
        tasks = get_rec_tasks()
        for i in range(len(tasks)):
            for j in range(len(tasks[i])):
                file.write("|" + str(tasks[i][j]))
            file.write("|\n")
