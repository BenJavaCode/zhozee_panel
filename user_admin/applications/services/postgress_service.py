from ..persistence.dao import user_dao, postgresql_dao
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from .service_handlers import request_handler, responsebody

"""_summary_:
    Services used to get data from postgress db targets/services.
"""



@request_handler  
def get_users_and_privs():
    result = postgresql_dao.get_users_of_postgresql('external1')
    if result:
        return responsebody(payload=result, success=True)
    return responsebody(message_text='something failed :()', success=False)

    