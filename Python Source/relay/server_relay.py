#FidgetySo
import asyncio
from websockets.server import serve

import enums

import logging
logger = logging.getLogger('websockets')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

class RelayServer:
	def __init__(self, config, database):
		self.config = config.yaml_data
		self.db = database

		self.host = self.config['Connection']['Host']
		self.port = self.config['Connection']['RelayPort']

		self.timeout = self.config['Connection']['TimeoutLength']

		asyncio.run(self.run())

	def create_response(self, recieved):
		return "A Response"

	async def handler(self, websocket):
		recieved = await websocket.recv()
		print(type(recieved))

		response = self.create_response(recieved)

		await websocket.send(response)
	
	async def run(self):
		async with serve(self.handler, self.host, self.port) as server:
			await asyncio.Future()
