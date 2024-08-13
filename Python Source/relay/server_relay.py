#FidgetySo
import asyncio
from websockets.server import serve

import ast

import enums
from relay.methods import Crafter


class RelayServer:
    def __init__(self, config, database):
        self.config = config.yaml_data
        self.db = database

        self.crafter = Crafter(config, self.db)

        self.host = self.config['Connection']['Host']
        self.port = self.config['Connection']['RelayPort']

        self.timeout = self.config['Connection']['TimeoutLength']

        asyncio.run(self.run())

    async def create_response(self, recieved, websocket):
        try:
            recieved = ast.literal_eval(recieved)
        except Exception as e:
            print("Improper format for dict conversion: ", recieved)
            print(e)
            return 'Uh Oh'

        # Client New/Update Crafting Request
        if recieved['method'] == 'c_new_crafting':
            response =  await self.crafter.c_new_crafting(websocket, recieved)
        else:
            response = dict(method="status", code=400, message="Unknown Method")
        return str(response)

    async def handler(self, websocket):
        recieved = await websocket.recv()
        response = await self.create_response(recieved, websocket)
        print(response)
        await websocket.send(response)
    
    async def run(self):
        async with serve(self.handler, self.host, self.port):
            await asyncio.Future()
