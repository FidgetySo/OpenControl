# FidgetySo
import asyncio
import websockets
import socket

import enums



class ClientRelay:
	def __init__(self, config, database):
		self.config = config.yaml_data
		self.db = database

		self.host = self.config['Connection']['Host']
		self.port = self.config['Connection']['RelayPort']
		self.host = host = f"ws://{self.host}:{self.port}"

		self.timeout = self.config['Connection']['TimeoutLength']
			

	async def send(self, data: dict):
		async with websockets.connect(self.host, ping_timeout=self.timeout) as websocket:
			await websocket.send(str(data))
			response = await websocket.recv()
			return response
