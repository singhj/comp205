# target.py

from connection import ApiConnection

class Target:
    def __init__(self, connection): # : ApiConnection
        self._conn = connection
        