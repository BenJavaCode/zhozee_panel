from .. import db
from flask_login import UserMixin

"""_summary_:
    Object models for relational database, compatible with MySQL or PostrgeSQL.
"""

class User(db.Model, UserMixin):
    __bind_key__ = None

    # Unique
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    # Non unique
    password = db.Column(db.String(254), nullable=False)
    
    def __repr__(self):
        return 'Username: '.format(
            self.username,
        )
    

