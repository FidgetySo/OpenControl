#import selectors
import socket
from threading import Thread

from websocket import create_connection
#import traceback

import enums

import time

#from relay.lib_client import Message


class ClientRelay:
	def __init__(self, config, database):
		self.config = config.yaml_data
		self.db = database

		self.host = self.config['Connection']['Host']
		self.port = self.config['Connection']['RelayPort']
		self.addr = (self.host, self.port)

		self.timeout = self.config['Connection']['TimeoutLength']

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((self.host, self.port))

		host = f"ws://{self.addr}/"
		ws = websocket.WebSocketApp(
			host,
			on_open=self.on_open,
			on_message=self.on_message,
			on_error=self.on_error,
			on_close=self.on_close,
			socket=self.sock
		)

		ws.run_forever(ping_timeout=self.timeout)

	def on_open(self, ws):
		def run(*args):
			open_message = dict(method="connect_client")
			ws.send(str(open_message))
		Thread(target=run).start()

	def send_request(self, request: dict):
		self.ws.send(str(request))
		response = self.ws.recv()
		return response