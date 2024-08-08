from enum import Enum

class RESPONSES(Enum):
    SUCCESS = 0
    GENERIC_ERROR = 1
    TIMED_OUT = 2
    INVALID_FORMAT = 3

class TABLES(Enum):
    REQUESTS = 0
    STORAGE = 1
    CRAFTING = 2
    POWER = 3