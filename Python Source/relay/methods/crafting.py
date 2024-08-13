import asyncio
import ast

from relay.methods import BasicMethod
import enums

class Crafter(BasicMethod):
    def __init__(self, config, database):
        super().__init__(config, database)
        self.allow_overloading = self.config['Crafting']['Queue']['AllowOverloadingRequests']

    async def c_new_crafting(self, websocket, recieved : dict):
        item = recieved['item']
        amount = recieved['amount']
        push = recieved['push']

        n_procs, _ = await self.g_new_crafting(websocket, item, amount, push)

        self.db.add_crafting_request(item, amount, n_procs)
        """
        data = dict(
            item=item,
            amount=amount,
            n_procs=n_procs
        )
        """
        response = dict(
            method="status",
            code=200,
            message="Succesfully Added New Crafting Request to the Queue"
        )
        return response
    
    
    async def g_new_crafting(self, websocket, item: str, amount: int, push: bool):
        if self.offline:
            #if self.allow_overloading:
            request = str(dict(
                method="g_new_crafting",
                item=item,
                amount=amount,
                push=push
            ))
            await websocket.send(request)
            g_response = await websocket.recv()
        
            g_response = ast.literal_eval(recieved)

            return n_procs, status
        else:
            return 1, "debug"

    #def d_new_crafting(self, recieved):

    """
    def c_update_crafting(self, recieved: dict):
        response = 
        return response
    def g_update_crafting(self, recieved: dict):
        response = 
        return response
    """
