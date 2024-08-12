# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 23:34:39 2024

@author: Fidgety
"""

class BasicMethod:
    def __init__(self, config, database):
        self.config = config.yaml_data
        self.db = database
