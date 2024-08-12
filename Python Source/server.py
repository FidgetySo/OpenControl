from db.db import DB
from config import Config

from relay.server_relay import RelayServer

if __name__ == "__main__":
	config = Config()
	database = DB(config)

	verbose = config.yaml_data['Debug']['VerboseLevel']
	if verbose > 0:
		import logging
		logger = logging.getLogger('websockets')

		if verbose == 1:
			logger.setLevel(logging.INFO)
		elif verbose == 2:
			pass
		elif verbose == 3:
			logger.setLevel(logging.DEBUG)
		else:
			logger.setLevel(logging.INFO)
		logger.addHandler(logging.StreamHandler())
	RelayServer(config, database)
