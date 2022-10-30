#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def tel_symbol_check(tel):
    syms = ('(', ')', '-')
    index = [0]
    for i in range(len(syms)):
        index.append(tel.find(syms[i]))

    index.append((tel.rfind(syms[-1])))
    index.append(len(tel))
    
    for i in range(len(index) - 1):
        if index[i] >= index[i + 1]:
            return False

    #print(index)

    for i in range(len(index) - 1):
        #print(tel[index[i] + 1 : index[i + 1]])
        #print(tel[index[i] + 1 : index[i + 1]].isdigit())
        if not(tel[index[i] + 1 : index[i + 1]].isdigit()):
            return False
    else:
        return True
#----------------------------------------------------------------------------
def role_symbol_check(role):
    for i in range(1, len(role) - 1):
        match role[i]:
            case ' ':
                if not(role[i + 1].isalpha() or role[i + 1].isdigit()):
                    return False
            case '-':
                if not(role[i + 1].isalpha() or role[i + 1].isdigit()):
                    return False    
            case _:
                if not(role[i].isalpha() or role[i].isdigit()):
                    return False
    else:
        return True
#----------------------------------------------------------------------------
def name_symbol_check(name):
    for i in range(1, len(name) - 1):
        match name[i]:
            case ' ':
                if not(name[i + 1].isalpha() or (name[i + 1] == "'")):
                    return False
            case '-':
                if not(name[i + 1].isalpha()):
                    return False    
            case "'":
                if not(name[i + 1].isalpha() or (name[i + 1] == " ")):
                    return False
            case _:
                if not(name[i].isalpha()):
                    return False
    else:
        return True
#----------------------------------------------------------------------------
def valid_id(str_data):
    str_data = str_data.strip()
    return str_data.isdigit() and (int(str_data) > 0)
#----------------------------------------------------------------------------
def valid_name(str_data):
    str_data = str_data.strip()
    if str_data[0].isupper() or ((str_data[0] == "'") and str_data[1].isupper()):
        if str_data[-1].isalpha() or ((str_data[-1] == "'") and str_data[-2].isalpha()):
            return name_symbol_check(str_data)
        else:
            return False
    else:
        return False
#----------------------------------------------------------------------------
def valid_role(str_data):
    str_data = str_data.strip()
    if str_data[0].isupper():
        if str_data[-1].isalpha() or str_data[-1].isdigit():
            return role_symbol_check(str_data)
        else:
            return False
    else:
        return False
#----------------------------------------------------------------------------
def valid_phone(str_data):
    str_data = str_data.strip().replace('\t', '').replace(' ', '')
    if str_data[0] == '+':
        return tel_symbol_check(str_data)
    else:
        return False
#----------------------------------------------------------------------------
