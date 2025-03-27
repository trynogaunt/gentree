import sqlite3
from pathlib import Path

class Database:
    _instance = None
    _initialized = False

    def __new__(cls, db_path: str = "C:\Users\Quentin\Desktop\Github\gentree\src\data\db.sqlite"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db_path: str = "C:\Users\Quentin\Desktop\Github\gentree\src\data\db.sqlite"):
        if not self._initialized:
            self.db_path = Path(db_path)
            self.db_path.parent.mkdir(parents=True, exist_ok=True)
            self.connection = None
            self.cursor = None
            Database._initialized = True

    def connect(self):
        """Connect to the SQLite database."""
        if not self.connection:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None

    def execute_query(self, query: str, params: tuple = ()) -> list:
        """Execute a query and return the results."""
        if not self.connection:
            self.connect()
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def execute_update(self, query: str, params: tuple = ()) -> None:
        """Execute an update query and commit changes."""
        if not self.connection:
            self.connect()
        self.cursor.execute(query, params)
        self.connection.commit()

    def __enter__(self):
        """Context manager entry."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()