from enums import

class ClientRelay:
	def __init__(self, config):
		self.config = config

		self.port = config['Connection']['RelayPort']
	def send_pac
	def send_crafting(self, item, amount=1, push=False):
		"""
		Steps
		1. Generate Packet String
		2. Send Packet String to relay server
			a. Relay server recieves packet
		3. Recieve Response Packet
		4. 
		"""
		# Generate Packet String
		packet_str =
		# Send Packet and Recieve Packet
		reponse =

	def recieve_crafting(self):
		return response_code, item, remaining,  