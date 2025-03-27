import tkinter as tk
from tkinter import ttk
from src.database.database import Database
from src.classes.character import Character

class CharacterList(tk.Frame):
    def __init__(self, parent, characters: list[Character] = None):
        super().__init__(parent)
        self.parent = parent
        
        self.button = ttk.Button(self, text="Add Character", command=self.add_character)
        self.button.pack(pady=10)
        for character in characters:
            print(character.full_name)
            # Display character information in the GUI
            character_frame = ttk.Frame(self)
            character_frame.pack(pady=5, padx=10, fill=tk.X)
            character_label = ttk.Label(character_frame, text=character.full_name)
            character_label.pack(side=tk.LEFT, padx=5)
            character_button = ttk.Button(character_frame, text="Edit", command=self.update_character)
            character_button.pack(side=tk.LEFT, padx=5)
        
    def add_character(self):
        # Logic to add a character to the list
        pass
    def remove_character(self):
        # Logic to remove a character from the list
        pass
    def update_character(self):
        # Logic to update a character in the list
        pass
    def display_characters(self):
        # Logic to display the list of characters
        pass
    def search_character(self):
        # Logic to search for a character in the list
        pass
    def sort_characters(self):
        # Logic to sort the list of characters
        pass
    def filter_characters(self):
        # Logic to filter the list of characters
        pass
    def get_characters(self):
        connection = Database()
        connection.connect()
        query = "SELECT * FROM characters"
        characters = connection.execute_query(query)
        connection.close()
        return characters
    
        