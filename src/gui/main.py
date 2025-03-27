import tkinter as tk
from tkinter import ttk
from src.gui.character_list import CharacterList
from src.classes.character import Character

class App(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.characters : list[Character]= Character.get_characters()
        self.pack( fill=tk.BOTH, expand=True )
        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack( fill=tk.BOTH, expand=True )
        
        self.character_frame = CharacterList(self.notebook, self.characters)
        self.tree_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.tree_frame, text="Family Tree")
        self.notebook.add(self.character_frame, text="Character")
        
        self.create_menu()
        
    def create_menu(self):
        menubar = tk.Menu(self.master)

        self.master.config(menu=menubar)
