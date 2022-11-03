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
        if column > (len(search_list) - 1):
            return -1
        else:
            cur_len = len(search_list[i][column])
            if max_sym_num < cur_len:
                max_sym_num = cur_len
    return (max_sym_num // 10 + 1) * 10
#-----------------------------------------------------------------------------
def auth_table_board(c1, c2):
    print('_' * (c1 + c2 + 4))
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