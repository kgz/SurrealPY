from datetime import datetime

from .db import db


class Account:
    id: str
    name: str
    balance: int
    opened: bool = False
    epoch_created: int


    def __init__(self, id: str, name: str, balance: int = 0, opened: bool = False, epoch_created: str = None) -> None:

        if not epoch_created:
            # now as ISO-88601 
            epoch_created = datetime.now().isoformat()
        self.id = id
        self.name = name
        self.balance = balance
        self.opened = opened
        self.epoch_created = epoch_created
    
    # @staticmethod
    # async def get(id: str) -> dict:
    #     database = db()
    #     return await database.select_one('clients', id)

    @staticmethod
    async def add(owner_id:str, data: dict = {}) -> dict:
        database = db()
        ret =  await database.create_one('accounts', database.idv4(), data)
        query ='RELATE {}->user_accounts->{};'.format(owner_id, ret['id'])
        print(query)
        await database.execute(query)
        return ret


    def todict(self) -> dict:
        return {
            "name": self.name,
            "balance": self.balance,
            "opened": self.opened,
            "epoch_created": self.epoch_created
        }