from src.database.DatabaseInterface import DatabaseInterface
from dataclasses import dataclass, field
from typing import Optional
@DatabaseInterface(table="characters")
@dataclass
class Character:
    firstname: str
    lastname: str
    lineage: str
    generation: int
    age: int
    job: str
    titles: list[str]
    picture: Optional[str] = None
    id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    def __post_init__(self):
        if isinstance(self.titles, str):
            self.titles = self.titles.split(',')
        elif not self.titles:
            self.titles = []

        self.titles = list(set(title.strip() for title in self.titles if title.strip()))

        if not self.picture:
            self.picture = "default.png"
    
    def __repr__(self):
        return f"Character({self.firstname}, {self.lastname}, {self.lineage}, {self.generation}, {self.age}, {self.job}, {self.picture})"
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
