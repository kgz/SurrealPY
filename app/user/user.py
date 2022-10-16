from typing import List

from flask_login import AnonymousUserMixin, UserMixin
from modules.database import database
from surrealdb.common.exceptions import SurrealException

# class User(UserMixin, AnonymousUserMixin):
#     db : database = database()
#     username: str
#     # is_active = True
#     # is_anonymous = False
#     # is_authenticated = False    
    
#     def __init__(self, username) -> None:
#         self.username = username
    

#     @staticmethod
#     async def signup(username, email, password) -> 'User':

#         q = f"""
#             CREATE user:{username} SET name = '{username}', email = '{email}', password = crypto::argon2::generate("{password}")
#         """
#         try:
#             db = database()
#             await db.execute(q)
#             user = User(username)
#             return user
#         except SurrealException as e:
#             return False


#     @staticmethod
#     async def get(username):
#         q = f"""
#             SELECT * FROM user:{username}
#         """
#         # db = database()

#         # await db.execute(q)
#         #TODO validate it exists
#         return User(username)

    





class User(UserMixin):
    def __init__(self, id_, name = '', email='', admin=False, picture=None):
        self.id = id_
        self.name = name
        self.email = email
        self.admin = admin
        self.picture = picture

        
    def is_authenticated(self):
        return True

    @property
    def is_authenticated(self):
        return True
    

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def get(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        return None
    
    @staticmethod
    async def get(username):
        q = f"""
            SELECT * FROM user:{username}
        """
        db = database()

        r = await db.execute(q)

        if r:
        #TODO validate it exists
            return User(username)
        return AnonymousUser()

    @staticmethod
    async def check_password(username, password):
        q = f"""
            SELECT crypto::argon2::compare(password, "{password}") AS valid FROM user:{username}
        """
        db = database()
        item: List[dict] = await db.execute(q)
        # get first item
        if not item:
            return False
        
        item = item[0]
        if item.get('valid'):
            return item
        else:
            return False
        
    @staticmethod
    async def signup(username, email, password) -> 'User':

        q = f"""
            CREATE user:{username} SET name = '{username}', email = '{email}', password = crypto::argon2::generate("{password}")
        """
        try:
            db = database()
            await db.execute(q)
            user = User(username)
            return user
        except SurrealException as e:
            return False

    @property
    def __dict__(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "is_authenticated": self.is_authenticated,
            "is_active": self.is_active(),
            "admin": self.admin,
            "img": self.picture,
        }


class AnonymousUser(AnonymousUserMixin):
    def __init__(self):
        self.id = None
        self.name = None
        self.email = None
        self.admin = False
    
    def is_authenticated(self):
        return False

    @property
    def is_authenticated(self):
        return False

    def is_active(self):
        return False

    def is_anonymous(self):
        return True

    def get_id(self):
        return None

    def get(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        return None

    @property
    def __dict__(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "is_authenticated": self.is_authenticated,
        }