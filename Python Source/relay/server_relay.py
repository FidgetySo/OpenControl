import socket
import selectors


import enums
from relay.lib_server import Message

class RelayServer:
	def __init__(self, config, database):
		self.config = config.yaml_data
		self.db = database

		self.host = self.config['Connection']['Host']
		self.port = self.config['Connection']['RelayPort']

		self.timeout = self.config['Connection']['TimeoutLength']

		self.sel = selectors.DefaultSelector()

		self.start()
	
	def accept_wrapper(self, sock):
		conn, addr = sock.accept()
		print(f"Accepted connection from {addr}")
		conn.setblocking(False)
		message = Message(self.sel, conn, addr)
		self.sel.register(conn, selectors.EVENT_READ, data=message)

	def start(self):
		self.lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.lsock.bind((self.host, self.port))
		self.lsock.listen()
		print(f"Listening on {(self.host, self.port)}")
		self.lsock.setblocking(False)
		self.sel.register(self.lsock, selectors.EVENT_READ, data=None)

		while True:
			try:
				events = self.sel.select(timeout=None)
				for key, mask in events:
					if key.data is None:
						self.accept_wrapper(key.fileobj)
					else:
						message = key.data
						try:
							message.process_events(mask)
						except Exception:
							print(
								f"Main: Error: Exception for {message.addr}:\n"
								f"{traceback.format_exc()}"
							)
						message.close()
			except KeyboardInterrupt:
				self.sel.close()