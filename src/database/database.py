from dataclasses import dataclass, fields as dataclass_fields
import functools
from typing import Optional, Union, Type
from contextlib import ContextDecorator
import sqlite3
class Database(ContextDecorator):
    def __enter__(self):
        return self
    
    def __init__(self):
        super().__init__()
        self.connection = None
        self.cursor = None
        self.db_path = "/data/db.sqlite"
    
    def connect(self):
        if not self.connection:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
            return True
        return False
    
    def execute_query(self, query: str, params: tuple = ()) -> list:
        """Execute a query and return the results."""
        if not self.connection:
            return None
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def __exit__(self, *exc):
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None
        return False