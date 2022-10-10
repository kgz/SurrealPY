from .Account import Account
from .db import db


class Client:

    def __init__(self) -> None:
        self.db = db()
    
    @staticmethod
    async def get(id: str) -> dict:
        database = db()
        return await database.select_one('clients', id)

    @staticmethod
    async def add(data: dict = {}) -> dict:
        database = db()
        return await database.create_one('clients', database.idv4(), data)

    @staticmethod
    async def get_accounts(id: str) -> dict:
        database = db()
        return await database.execute('SELECT name, ->user_accounts->accounts.* as accounts FROM {}'.format(id))