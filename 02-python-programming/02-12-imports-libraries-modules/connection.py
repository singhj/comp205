# connection.py

from target import Target

class ApiConnection:
    def get_target(self):
        return Target(connection=self)
    