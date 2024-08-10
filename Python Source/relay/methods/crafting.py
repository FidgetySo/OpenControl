import enums

class Crafter:
	def __init__(self, config, database):
		self.db = database

		self.allow_overloading = config['Crafting']['Queue']['AllowOverloadingRequests']

	def c_new_crafting(self, recieved : dict):
		#g_response = self.g_new_crafting(recieved)
		
		item = recieved['item']
		amount = recieved['amount']
		#n_bytes = g_response['n_bytes']
		#n_procs = g_response['n_procs']
		n_bytes = 1024
		n_procs = 1

		self.db.add_crafting_request(item, amount, n_bytes, n_procs)

		data = dict(
			item=item,
			amount=amount,
			n_bytes=n_bytes,
			n_procs=n_procs
		)

		response = dict(
			method="status",
			code=200,
			message="Succesfully Added New Crafting Request to the Queue"
		)
		return response
	"""
	def c_update_crafting(self, recieved: dict):
		response = 
		return response

	def g_new_crafting(self, recieved: dict):
		response = 
		return resposne

	def g_update_crafting(self, recieved: dict):
		response = 
		return response
"""