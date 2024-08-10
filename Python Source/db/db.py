import sqlite3

from enums import TABLES

class DB:
	def __init__(self, config):
		self.write_config = config.write
		self.config = config.yaml_data['Database']

		self.connect()

	def connect(self):
		self.database_file = self.config['DB']
		print('Loading Database' + self.database_file)
		self.db_connection = sqlite3.connect(self.database_file)
		self.cursor = self.db_connection.cursor()
		print('Loaded Database')

	def get_table_data(self, table):
		if table == TABLES.REQUESTS:
			table = self.config['Requests']
		elif table == TABLES.STORAGE:
			table = self.config['Storage']
		elif table == TABLES.CRAFTING:
			table = self.config['Crafing']
		elif table == TABLES.CRAFTABLES:
			table = self.config['Craftables']
		elif table == TABLES.POWER:
			table = self.config['Power']
		else:
			table = None
			print('Invalid Table')
			return

		table_query_str = 'SELECT * from {0}'.format(table)
		table_query = self.cursor.execute(table_query_str)
		
		return table_query

	def add_crafting_request(self, item, amount, datetime):
		pass
	def update_crafting_request(
		self,
		id,
		remaining,
		n_bytes,
		n_procs,
		amount=None
	):
		update_str = ''
		self.cursor.execute(update_str)

	def get_craftables(self):
		craftables_query = self.get_table_data(TABLES.CRAFTABLES)
		
		craftables = []
		for item in craftables_query:
			craftables.append(item[0])
		return craftables

