import os
from datetime import datetime

from enums import TABLES

class DB:
	def __init__(self, config):
		self.write_config = config.write
		self.config = config.yaml_data['Database']

		# Is it a local sqlite3 database?
		self.is_local = self.config['Local']

		self.new_database = False
		self.connect()

	def connect(self):
		if self.is_local:
			import sqlite3
			# Load Databse from file
			self.database_file = self.config['DB']

			if os.path.exists(self.database_file):
				print('Loading Local Database ' + self.database_file)
				self.new_database = False
			else:
				print('Creating Local Database ' + self.database_file)
				self.new_database = True

			self.db_connection = sqlite3.connect(self.database_file)
			self.cursor = self.db_connection.cursor()

			# Check if tables exist
			existing_tables = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
		else:
			# Connect to remote database
			import mysql.connector

			print("Connecting to Remote Database")
			self.db_connection = mysql.connector.connect(
				host=self.config['Host'],
				port=self.config['Port'],
				database=self.config['RemoteDB'],
				user=self.config['Username'],
				password=self.config['Password']
				)
			self.cursor = self.db_connection.cursor()

			#Check if tables exist
			self.cursor.execute("SHOW TABLES;")
			existing_tables = self.cursor.fetchall()
		try:
			tables_list = [item[0] for item in existing_tables]
			if len(tables_list) < 5:
				self.new_database = True
			else:
				pass
		except Exception as e:
			print(e)
			self.new_database = True
		if self.new_database:
			self.create_tables()
			print('Loaded Database and Created Tables ')
		else:
			print('Loaded Database')

			


	def create_tables(self):
		self.cursor.execute("DROP TABLE IF EXISTS "+self.config['Storage']+"")
		self.cursor.execute("DROP TABLE IF EXISTS "+self.config['Crafting']+"")
		self.cursor.execute("DROP TABLE IF EXISTS "+self.config['Craftables']+"")
		self.cursor.execute("DROP TABLE IF EXISTS "+self.config['Power']+"")
		self.cursor.execute("DROP TABLE IF EXISTS "+self.config['Requests']+"")
		# Create Tables
		storage_str = f"""CREATE TABLE {self.config['Storage']} (
			item    	TEXT,
			amount    	INTEGER,
			data    	TEXT
			);"""
		crafting_str = f"""CREATE TABLE {self.config['Crafting']} (
			item		TEXT,
			amount		INTEGER,
			remaining	INTEGER,
			n_procs		INTEGER,
			datatime	TEXT, 
			c_id		INTEGER
			);"""
		craftables_str = f"""CREATE TABLE {self.config['Craftables']} (
			item		TEXT
			);"""
		power_str = f"""CREATE TABLE {self.config['Power']} (
			id 			INTEGER,
			total_eu	INTEGER,
			input_eu	INTEGER
			);"""
		requests_str = f"""CREATE TABLE {self.config['Requests']} (
			item  		TEXT,
			amount    	INTEGER,
			status    	INTEGER,
			datetime  	INTEGER,
			c_id  		INTEGER
		);"""

		self.cursor.execute(storage_str)
		self.cursor.execute(crafting_str)
		self.cursor.execute(craftables_str)
		self.cursor.execute(power_str)
		self.cursor.execute(requests_str)

		self.db_connection.commit()


	def get_table_data(self, table):
		if table == TABLES.STORAGE:
			table = self.config['Storage']
		elif table == TABLES.CRAFTING:
			table = self.config['Crafting']
		elif table == TABLES.CRAFTABLES:
			table = self.config['Craftables']
		elif table == TABLES.POWER:
			table = self.config['Power']
		elif table == TABLES.REQUESTS:
			table = self.config['Requests']
		else:
			table = None
			print('Invalid Table')
			return

		table_query_str = 'SELECT * from {0}'.format(table)
		self.cursor.execute(table_query_str)
		table_query = self.cursor.fetchall()
		return table_query

	def add_crafting_request(
		self,
		item,
		amount,
		n_procs
	):
		amount = str(amount)
		n_procs = str(n_procs)
		now = datetime.now()
		date_time = now.strftime("%m/%d/%Y.%H:%M:%S")
		c_id = str(
			len(
				list(self.get_table_data(TABLES.CRAFTING))
			) +
			len(
				list(self.get_table_data(TABLES.REQUESTS))
			) + 1
		)
		add_str = "INSERT INTO "+self.config['Crafting']+" VALUES('"+item+"', "+amount+", "+amount+", "+n_procs+", '"+date_time+"', '"+c_id+"');"

		self.cursor.execute(add_str)
		self.db_connection.commit()

	def update_crafting_request(
		self,
		remaining,
		c_id,
		amount=None
	):
		if not amount:
			try:
				# Get amount from database
				crafting_query = self.get_table_data(TABLES.CRAFTING)
				for i in crafting_query:
					if i[6] == c_id:
						amount = i[1]
			except:
				print("Invalid Crafting ID")
		update_str = "UPDATE "+self.config['crafting']+" SET remaining = '"+remaining+"' WHERE c_id = '"+c_id+"';"
		print(update_str)
		self.cursor.execute(update_str)
		self.db_connection.commit()

	def get_craftables(self):
		craftables_query = self.get_table_data(TABLES.CRAFTABLES)
		
		craftables = []
		for item in craftables_query:
			craftables.append(item[0])
		return craftables
	
	def update_craftables(self, items: list):
		# Delete All Craftables (easier to program might switch to something more effiecent later)
		self.cursor.execute(f"SELECT * FROM {self.config['Craftables']};")
		self.cursor.execute(f"DELETE FROM {self.config['Craftables']};")

		for item in items:
			add_item_str = "INSERT INTO "+self.config['Craftables']+" VALUES('"+item+"');"
			self.cursor.execute(add_item_str)
		self.db_connection.commit()


	def get_power(self):
		self.cursor.execute("SELECT * from "+self.config['Power']+" ORDER BY id DESC LIMIT 1")
		power_row = self.cursor.fetchone()
		#power_time = power_row[0]
		try:
			for i in power_row:
				total_power = i[1]
				input_power = i[2]
			return total_power, input_power
		except:
			return 0, 0
