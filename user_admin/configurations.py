DATABASE_URL = "postgresql://admin:admin@localhost:5432/user_admin"

BINDS = {
    'external1':"postgresql://admin:admin@localhost:5432/postgres4_testdummy",
}

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'change_me_goddammit'
    SQLALCHEMY_DATABASE_URI = DATABASE_URL

    @property
    def SQLALCHEMY_DATABASE_URI(self):  # Note: all caps
        return DATABASE_URL
    
    @property
    def SQLALCHEMY_BINDS(self):
        return BINDS

class DevelopmentConfig(Config):
    #DB_SERVER = 'localhost'
    pass