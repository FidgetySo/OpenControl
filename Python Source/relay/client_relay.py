from enums import

class ClientRelay:
	def __init__(self, config):
		self.config = config

		self.port = config['Connection']['RelayPort']