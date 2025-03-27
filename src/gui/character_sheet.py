import tkinter as tk
from tkinter import ttk
from src.classes.character import Character
class CharacterSheet(tk.Toplevel):
    def __init__(self, parent, character: 'Character' = None, editable : bool =False):
        super().__init__(parent)
        self.parent = parent
        self.character = character
        self.editable = editable
        self.title("Character Sheet")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.cancel_character)


        if editable:
            self.create_editable_character_sheet()
        else:
            self.create_character_sheet()
        
    def create_character_sheet(self):
        firstname_label = ttk.Label(self, text="First Name:")
        firstname_text = ttk.Label(self, text=self.character.firstname)
        lastname_label = ttk.Label(self, text="Last Name:")
        lastname_text = ttk.Label(self, text=self.character.lastname)
        lineage_label = ttk.Label(self, text="Lineage:")
        lineage_text = ttk.Label(self, text=self.character.lineage)
        generation_label = ttk.Label(self, text="Generation:")
        generation_text = ttk.Label(self, text=self.character.generation)
        age_label = ttk.Label(self, text="Age:")
        age_text = ttk.Label(self, text=self.character.age)
        job_label = ttk.Label(self, text="Job:")
        job_text = ttk.Label(self, text=self.character.job)
        titles_label = ttk.Label(self, text="Titles:")
        titles_text = ttk.Label(self, text=", ".join(self.character.titles))
        firstname_label.pack(pady=5, padx=10, anchor=tk.W)
        firstname_text.pack(pady=5, padx=10, anchor=tk.W)
        lastname_label.pack(pady=5, padx=10, anchor=tk.W)
        lastname_text.pack(pady=5, padx=10, anchor=tk.W)
        lineage_label.pack(pady=5, padx=10, anchor=tk.W)
        lineage_text.pack(pady=5, padx=10, anchor=tk.W)
        generation_label.pack(pady=5, padx=10, anchor=tk.W)
        generation_text.pack(pady=5, padx=10, anchor=tk.W)
        age_label.pack(pady=5, padx=10, anchor=tk.W)
        age_text.pack(pady=5, padx=10, anchor=tk.W)
        job_label.pack(pady=5, padx=10, anchor=tk.W)
        job_text.pack(pady=5, padx=10, anchor=tk.W)
        titles_label.pack(pady=5, padx=10, anchor=tk.W)
        titles_text.pack(pady=5, padx=10, anchor=tk.W)

    
    def create_editable_character_sheet(self):
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

        if self.character:
            self.firstname_entry.insert(0, self.character.firstname)
            self.lastname_entry.insert(0, self.character.lastname)
            self.lineage_entry.insert(0, self.character.lineage)
            self.generation_entry.insert(0, self.character.generation)
            self.age_entry.insert(0, self.character.age)
            self.job_entry.insert(0, self.character.job)
            self.titles_entry.insert(0, ", ".join(self.character.titles))
        save_button = ttk.Button(self, text="Save", command= lambda : self.save_character())
        save_button.pack(pady=10, padx=10, anchor=tk.W)
        cancel_button = ttk.Button(self, text="Cancel", command=self.cancel_character)
        cancel_button.pack(pady=10, padx=10, anchor=tk.W)



    def save_character(self):
        self.character.update(
            firstname=self.firstname_entry.get(),
            lastname=self.lastname_entry.get(),
            lineage=str(self.lineage_entry.get()),
            generation=int(self.generation_entry.get()),
            age=int(self.age_entry.get()),
            job=self.job_entry.get(),
            titles=self.titles_entry.get().split(", ")
        )
        self.destroy()
    
    def cancel_character(self):
        self.destroy()