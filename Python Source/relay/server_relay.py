import socket

import enums

class RelayServer:
	def __init__(self, config, database):
		self.config = config
		self.db = database

		self.relay_port = config['Connection']['RelayPort']
		self.host = '127.0.0.1'

	def start(self)
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((self.host, self.relay_port))
		s.listen()
		conn, addr = s.accept()
		with conn:
			print(f"Connected by {addr}")
			while True:
				data = conn.recv(1024)
			if not data:
                break
            decoded_data = decode_packet(data)
            handled = handle_data(decoded_data)

    def decode_packet(self, packet):
    	pass

    def handle_data(self, data):
    	if data['method'] == 'update_crafting':
    		self.db.
    	elif data['method'] == 'update_storage':
    		self.