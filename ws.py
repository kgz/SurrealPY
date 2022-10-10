
# create a new client to connect to SurrealDB
from surrealdb.clients.ws import WebsocketClient

client = WebsocketClient("ws://localhost:8000")
import socketio


async def main():

    await client.signin({"namespace": "test", "database": "test", "username": "root", "password": "root"})
    await client.connect()

    # sio = socketio.AsyncClient()
    # # --user root --pass root
    # await sio.connect('ws://localhost:8000', auth={'username': 'root', 'password': 'root'}, namespaces=['/test/test'])



if __name__ == "__main__":
    import asyncio

    asyncio.run(main())