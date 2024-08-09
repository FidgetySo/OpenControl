from enum import Enum

class RESPONSES(Enum):
    SUCCESS = 0
    GENERIC_ERROR = 1
    TIMED_OUT = 2
    INVALID_FORMAT = 3

class METHODS(Enum):
    ADD_CRAFTING = 0
    UPDATE_CRAFTING = 1
    UPDATE_STORAGE = 2
    INPUT_POWER = 3
    TOTAL_POWER = 4

class TABLES(Enum):
    REQUESTS = 0
    STORAGE = 1
    CRAFTING = 2
    CRAFTABLES = 3
    POWER = 4