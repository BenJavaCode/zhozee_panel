from ..persistence.dao import user_dao
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from .service_handlers import request_handler, responsebody

"""_summary_:
    User services, that either query or manipulate data in User object model.
    used primarily by routing layer, but also by other services.
"""

@request_handler  
def login(password, username):
    user = user_dao.get_first_where(username=username)
    if user:
        if __check_password_correct(specified_password=password, user=user):
            login_user(user, remember=True)
            return responsebody(message_text='Logged in', success=True)
        else: return responsebody(message_text='Password incorrect', success=False)
    else: return responsebody(message_text='User does not exist', success=False)
    
@request_handler
def current_user_repr(exclude=['password']):
    user_repr = user_dao.current_user_repr()
    if exclude:
        user_repr = {key:val for (key,val) in user_repr.items() if key not in exclude}
        return responsebody(success=True, payload=user_repr)
    return responsebody(success=True, payload=user_repr)



def __check_password_correct(specified_password, user=False):
    if user: 
        password = user.password
    else: 
        password = user_dao.get_user_attr('password')
    return check_password_hash(password, specified_password)


    
