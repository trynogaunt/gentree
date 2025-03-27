import tkinter as tk
from tkinter import ttk

from src.classes.character import Character

class CharacterAdd(tk.Toplevel):
    def __init__(self, parent, character: Character = None):
        super().__init__(parent)
        self.parent = parent
        self.character = character
        self.title("Add Character")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.cancel_character)

        self.create_character_sheet()

    def create_character_sheet(self):
        # Create labels and entries for character attributes
        self.firstname_label = ttk.Label(self, text="First Name:")
        self.firstname_entry = ttk.Entry(self)
        self.firstname_label.pack(pady=5, padx=10, anchor=tk.W)
        self.firstname_entry.pack(pady=5, padx=10, anchor=tk.W)

        self.lastname_label = ttk.Label(self, text="Last Name:")
        self.lastname_entry = ttk.Entry(self)
        self.lastname_label.pack(pady=5, padx=10, anchor=tk.W)
        self.lastname_entry.pack(pady=5, padx=10, anchor=tk.W)

        self.lineage_label = ttk.Label(self, text="Lineage:")
        self.lineage_entry = ttk.Entry(self)
        self.lineage_label.pack(pady=5, padx=10, anchor=tk.W)
        self.lineage_entry.pack(pady=5, padx=10, anchor=tk.W)

        self.generation_label = ttk.Label(self, text="Generation:")
        self.generation_entry = ttk.Entry(self)
        self.generation_label.pack(pady=5, padx=10, anchor=tk.W)
        self.generation_entry.pack(pady=5, padx=10, anchor=tk.W)

        self.age_label = ttk.Label(self, text="Age:")
        self.age_entry = ttk.Entry(self)
        self.age_label.pack(pady=5, padx=10, anchor=tk.W)
        self.age_entry.pack(pady=5, padx=10, anchor=tk.W)

        self.job_label = ttk.Label(self, text="Job:")
        self.job_entry = ttk.Entry(self)
        self.job_label.pack(pady=5, padx=10, anchor=tk.W)
        self.job_entry.pack(pady=5, padx=10, anchor=tk.W)

        self.titles_label = ttk.Label(self, text="Titles:")
        self.titles_entry = ttk.Entry(self)
        self.titles_label.pack(pady=5, padx=10, anchor=tk.W)
        self.titles_entry.pack(pady=5, padx=10, anchor=tk.W)

        save_button = ttk.Button(self, text="Save", command=self.save_character())
