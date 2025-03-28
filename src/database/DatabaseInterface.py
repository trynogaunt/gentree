from dataclasses import dataclass, fields as dataclass_fields
import functools
from typing import Optional, Union, Type
from contextlib import ContextDecorator
import sqlite3
from src.database.database import Database

class DatabaseInterface:
    def __init__(self, table: str = None, key_column: str = "id"):
        assert(table)
        assert(key_column)
        self.table = table
        self.key_column = key_column
    
    def get_table(self) -> str:
        return self.table

    def get_key(self) -> str:
        return self.key_column
    
    def get_all_by[Cls](self, cls: Type[Cls], **kwargs) -> list[Cls]:
        with Database() as db:
            db.connect()
        

            query = f"""
                SELECT c.*, GROUP_CONCAT(t.title) as titles
                FROM {self.table} c
                LEFT JOIN titles t ON c.id = t.character_id
            """
            
        
            if len(kwargs) > 0:
                key_generator = ('c.{} = ?'.format(kw) for kw in kwargs.keys())
                query += f" WHERE {' AND '.join(key_generator)}"
            
            query += " GROUP BY c.id"
            rows = db.execute_query(query, tuple(kwargs.values()) if kwargs else ())
        
            columns_query = f"PRAGMA table_info({self.table})"
            columns = db.execute_query(columns_query)
            column_names = [col[1] for col in columns]
            column_names.append('titles')  
            

            result = []
            for row in rows:
                row_data = {column_names[i]: row[i] for i in range(len(column_names)-1)}
                titles_str = row[-1] 
                row_data['titles'] = titles_str.split(',') if titles_str else []
                result.append(cls(**row_data))
                
            return result
    
    def get_all[Cls](self, cls : Type[Cls]) -> list[Cls]:
        return self.get_all_by(cls)
            
    
    def __call__(self, cls):
        cls.get_all = classmethod(self.get_all)
        cls.get_table = staticmethod(self.get_table)
        cls.get_key = staticmethod(self.get_key)
        
        return cls