import asyncio

# import the http client
from surrealdb.clients.http import HTTPClient

# create a new client to connect to SurrealDB
client = HTTPClient("http://localhost:8000", namespace="test", database="testtb", username="root",
                             password="root")

from modules import Account, Client
from modules.db import db

commands : dict = {
    "new client": Client.add,


}

# while 1:      
#     command = input("Enter command: ")daw
#     if command in commands:
#         r = asyncio.run(commands[command]())
#         print(r)
#     else:
#         print("Command not found")
async def main():
    cid = await Client.add(dict(name="Mike"))#accounts:⟨59e035e6-db67-45fd-876b-0468a2527bc2⟩
    database = db()

    # r = await Client.get_accounts("238a02cfcd274f4888b9bf47f43ab50a")
    # print(r)
    account = Account(database.idv4(), "test1")
    account = account.todict()
    r = await Account.add(cid['id'], account)
    account = Account(database.idv4(), "test2")
    account = account.todict()
    await Account.add(cid['id'], account)

    r = await Client.get_accounts(cid['id'])
    print(r)

    # # print(account.todict())   
    # database.execute("RELATE clients:238a02cfcd274f4888b9bf47f43ab50a->user_accounts->accounts:b1e6b728fddd4f0a8d2ed6703ee9e72f")
    # database.execute("RELATE accounts:59e035e6-db67-45fd-876b-0468a2527bc2->write->clients:885ea06a-cfa8-4580-a4a3-e82890b046ab")
    # database.execute("RELATE clients:test->write->article:surreal SET time.written = time::now();")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
