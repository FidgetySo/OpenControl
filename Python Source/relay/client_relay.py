import selectors
import socket

import enums

from relay.lib_client import Message

class ClientRelay:
	def __init__(self, config, database):
		self.config = config.yaml_data
		self.db = database

		self.host = self.config['Connection']['Host']
		self.port = self.config['Connection']['RelayPort']
		self.addr = (self.host, self.port)

		self.timeout = self.config['Connection']['TimeoutLength']

		self.sel = selectors.DefaultSelector()

		self.start_connection()

	def start_connection(self):
		print(f"Starting connection to {self.addr}")
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.setblocking(False)
		self.sock.connect_ex(self.addr)

		events = selectors.EVENT_READ | selectors.EVENT_WRITE
		self.sel.register(self.sock, events, data=None)

	def create_request(self, content: dict):
		return dict(
		type="text/json",
		encoding="utf-8",
		content=content,
	)

	def new_crafting_request(self, item: str, amount: int, push: bool):
		crafting_dict = dict(method="new_crafting", item=item, amount=amount, push=push)
		crafting_json = self.create_request(crafting_dict)
		#self.send_request(crafting_json)
		print(crafting_json)
	
	#def send_request(self, data):

		