import enums

class Crafter:
	def __init__(self, config):
		self.overloading = config['Crafting']['Queue']['AllowOverloadingRequests']

	def 