"""
import socket
import selectors
import traceback
"""

from websockets.sync.server import serve

import enums
#from relay.lib_server import Message

class RelayServer:
	def __init__(self, config, database):
		self.config = config.yaml_data
		self.db = database

		self.host = self.config['Connection']['Host']
		self.port = self.config['Connection']['RelayPort']

		self.timeout = self.config['Connection']['TimeoutLength']

		self.run()

	def handler(websocket):
		recieved = await websocket.recv()
		print(recieved)

		response = self.create_reponse(recieved)

		await websocket.send(response)

    def run(self):
    	with websockets.sync.server.serve(self.handler, self.addr, self.port) as server:
    		server.serve_forever()
