#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
'''
|manager_id|Name|Role|Telephone number|
|worker_id|Name|Role|Telephone number|Characteristics|
|task_id|Name|worker_id|manager_id|Description|
'''
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------
rec_list_workers = []
rec_list_managers = []
rec_list_tasks = []
#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def id_prepare(id):
    return id.strip()
#----------------------------------------------------------------------------
def name_and_role_prepare(line):
    return line.strip().replace('\t', ' ')
#----------------------------------------------------------------------------
def phone_prepare(tel):
    return tel.strip().replace('\t', '').replace(' ', '')
#----------------------------------------------------------------------------
def get_rec_workers():
    return rec_list_workers
#----------------------------------------------------------------------------
def get_rec_managers():
    return rec_list_managers
#----------------------------------------------------------------------------
def get_rec_tasks():
    return rec_list_tasks
#----------------------------------------------------------------------------
def append_rec_workers(element):

    rec_list_workers.append((id_prepare(element[0]), 
                                name_and_role_prepare(element[1]),
                                name_and_role_prepare(element[2]), 
                                phone_prepare(element[3]), 
                                element[4]))
#----------------------------------------------------------------------------
def append_rec_managers(element):

    rec_list_managers.append((id_prepare(element[0]), 
                                name_and_role_prepare(element[1]),
                                name_and_role_prepare(element[2]), 
                                phone_prepare(element[3])))
#----------------------------------------------------------------------------
def append_rec_tasks(element):

    rec_list_tasks.append((id_prepare(element[0]), 
                                name_and_role_prepare(element[1]),
                                id_prepare(element[2]), 
                                id_prepare(element[3]), 
                                element[4]))
#----------------------------------------------------------------------------
def is_in_list(search_obj, lst_search, column):
    for i in range(len(lst_search)):
        if lst_search[i][column] == search_obj:
            return int(lst_search[i][0])
    else:
        return -1
#----------------------------------------------------------------------------
def is_in_list_full(search_obj, lst_search, column):
    for i in range(len(lst_search)):
        if lst_search[i][column] == search_obj:
            return lst_search[i]
    else:
        return -1