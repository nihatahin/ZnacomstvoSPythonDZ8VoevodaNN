#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def valid_data_base(is_valid):
    if is_valid:
        print("Data base is succsessfully loaded!")
    else:
        print("INVALID data base! Loading process was interrupted!")
#-----------------------------------------------------------------------------
def max_in_db_sym_num(search_list, column):
    max_sym_num = 0
    for i in range(len(search_list)):
        if column > (len(search_list) + 1):
            return -1
        else:
            cur_len = len(search_list[i][column])
            if max_sym_num < cur_len:
                max_sym_num = cur_len
    return (max_sym_num // 10 + 1) * 10
#-----------------------------------------------------------------------------
def max_in_sym_num(search_list):
    max_sym_num = 0
    for i in range(len(search_list)):
        cur_len = len(str(search_list[i]))
        if max_sym_num < cur_len:
            max_sym_num = cur_len
    return (max_sym_num // 10 + 1) * 10
#-----------------------------------------------------------------------------
def auth_table_board(c1, c2):
    print('-' * (c1 + c2 + 4))
#----------------------------------------------------------------------------
def auth_table_hat(c1_width, c2_width):
    print('\nWorkBUG people schedule.')
    auth_table_board(c1_width, c2_width)
    cell_1 = 'Managees'
    cell_2 = 'Managers'
    print('|' + (c1_width - len(cell_1)) * ' ' + cell_1 + '||' + (c2_width - len(cell_2)) * ' ' + cell_2 + '|')
    auth_table_board(c1_width, c2_width)
#----------------------------------------------------------------------------
def auth_line(c1, c2, worker, manager):
    print('|' + worker.rjust(c1) + '||' + manager.rjust(c2) + '|')
#----------------------------------------------------------------------------
def auth_list(c1_width, c2_width, wrk_db, mng_db):
    empty_str = ''
    w_length = len(wrk_db)
    m_length = len(mng_db)
    for i in range(max(w_length, m_length)):
        auth_line(c1_width, c2_width, wrk_db[i][1] if i < w_length else empty_str, mng_db[i][1] if i < m_length else empty_str)
#----------------------------------------------------------------------------
def auth_msg_full(wrk_db, mng_db):
    cell_1_width = max_in_db_sym_num(wrk_db, 1)
    cell_2_width = max_in_db_sym_num(mng_db, 1)
    print('WorkBUG authentification procedure.')
    auth_table_hat(cell_1_width, cell_2_width)
    auth_list(cell_1_width, cell_2_width, wrk_db, mng_db)
    auth_table_board(cell_1_width, cell_2_width)
    print()
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
def task_table_board(c1, c2):
    print('-' * (c1 + c2 + 4))
#----------------------------------------------------------------------------
def task_table_hat(c1_width, c2_width):
    task_table_board(c1_width, c2_width)
    cell_1 = 'Task ID'
    cell_2 = 'Task name'
    print('|' + (c1_width - len(cell_1)) * ' ' + cell_1 + '||' + (c2_width - len(cell_2)) * ' ' + cell_2 + '|')
    task_table_board(c1_width, c2_width)
#----------------------------------------------------------------------------
def task_line(c1, c2, t1, t2):
    print('|' + t1.rjust(c1) + '||' + t2.rjust(c2) + '|')
#----------------------------------------------------------------------------
def task_list(c1_width, c2_width, t_data):
    t_length = len(t_data)
    for i in range(t_length):
        task_line(c1_width, c2_width, t_data[i][0], t_data[i][1])
#----------------------------------------------------------------------------
def task_msg_full(task_data):
    if len(task_data)  <= 0:
        print("You have no tasks!")
    else:
        cell_1_width = max_in_db_sym_num(task_data, 0)
        cell_2_width = max_in_db_sym_num(task_data, 1)
        task_table_hat(cell_1_width, cell_2_width)
        task_list(cell_1_width, cell_2_width, task_data)
        task_table_board(cell_1_width, cell_2_width)
    print()
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
def staff_table_board(c1, c2, c3, c4):
    print('-' * (c1 + c2 + c3 + c4 + 8))
#----------------------------------------------------------------------------
def staff_table_hat(c1_width, c2_width, c3_width, c4_width):
    staff_table_board(c1_width, c2_width, c3_width, c4_width)
    cell_1 = 'ID'
    cell_2 = 'Name'
    cell_3 = 'Role'
    cell_4 = 'Tasks'
    print('|' + (c1_width - len(cell_1)) * ' ' + cell_1 + '||' + (c2_width - len(cell_2)) * ' ' + cell_2 + 
    '||' + (c3_width - len(cell_3)) * ' ' + cell_3 + '||' + (c4_width - len(cell_4)) * ' ' + cell_4 + '|')
    staff_table_board(c1_width, c2_width, c3_width, c4_width)
#----------------------------------------------------------------------------
def staff_line(c1, c2, c3, c4, w1, w2, w3, t):
    print('|' + w1.rjust(c1) + '||' + w2.rjust(c2) + '||' + w3.rjust(c3) + '||' + t.rjust(c4) + '|')
#----------------------------------------------------------------------------
def staff_list(c1_width, c2_width, c3_width, c4_width, w_data, t_data):
    w_length = len(w_data)
    for i in range(w_length):
        staff_line(c1_width, c2_width, c3_width, c4_width, w_data[i][0], w_data[i][1], w_data[i][2], str(t_data[i]))
#----------------------------------------------------------------------------
def staff_msg_full(wrk, tsk_cnt):
    if len(wrk)  <= 0:
        print("You have no managees!")
    else:
        cell_1_width = max_in_db_sym_num(wrk, 0)
        cell_2_width = max_in_db_sym_num(wrk, 1)
        cell_3_width = max_in_db_sym_num(wrk, 2)
        cell_4_width = max_in_sym_num(tsk_cnt)
        staff_table_hat(cell_1_width, cell_2_width, cell_3_width, cell_4_width)
        staff_list(cell_1_width, cell_2_width, cell_3_width, cell_4_width, wrk, tsk_cnt)
        staff_table_board(cell_1_width, cell_2_width, cell_3_width, cell_4_width)
    print()
#----------------------------------------------------------------------------