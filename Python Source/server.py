import enums

from db.db import DB
from config import Config

from relay.server_relay import RelayServer

if __name__ == "__main__":
	config = Config()
	database = DB(config)

	RelayServer()