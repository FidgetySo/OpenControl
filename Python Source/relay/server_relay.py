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

		self.crafter = Crafter(self.config, self.db) 

		self.host = self.config['Connection']['Host']
		self.port = self.config['Connection']['RelayPort']

		self.timeout = self.config['Connection']['TimeoutLength']

		asyncio.run(self.run())

	def create_response(self, recieved):
		try:
			recieved = ast.literal_eval(recieved)
		except Exception as e:
			print("Improper format for dict conversion: ", recieved)
			print(e)
			return 'Uh Oh'

		# Client New/Update Crafting Request
		if recieved['method'] == 'c_new_crafting':
			response = self.crafter.c_new_crafting(recieved)
		elif recieved['method'] == 'c_update_crafting':
			response = self.crafter.c_update_crafting(recieved)

		# Game New/Update Crafting Request
		elif recieved['method'] == 'g_new_crafting':
			reponse = self.crafter.g_new_crafting(recieved)
		elif recieved['method'] == 'g_update_crafting':
			response = self.crafer.g_update_crafting(recieved)

		else:
			response = dict(method="status", code=400, message="Unknown Method")
		return str(response)

	async def handler(self, websocket):
		recieved = await websocket.recv()
		response = self.create_response(recieved)
		await websocket.send(response)
	
	async def run(self):
		async with serve(self.handler, self.host, self.port) as server:
			await asyncio.Future()
