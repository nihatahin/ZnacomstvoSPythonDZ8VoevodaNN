#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
import messages as msg
from base_func import import_full_base
from auth import auth_logic
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
import_success = import_full_base()
msg.valid_data_base(import_success)
#----------------------------------------------------------------------------
auth_logic()