import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
from src.classes.character import Character
class CharacterSheet(tk.Toplevel):
    def __init__(self, parent, character: 'Character' = None, editable : bool =False):
        super().__init__(parent)
        self.parent = parent
        self.character = character
        self.editable = editable
        self.title(self.character if self.character else "Character Sheet")
        self.geometry("400x500")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.cancel_character)

        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.info_frame = ttk.Frame(self.main_frame, border=1, width=200)
        self.info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.picture_frame = ttk.Frame(self.main_frame, border=1, relief=tk.SUNKEN, width=200)
        self.picture_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.fullname_label = ttk.Label(self.info_frame, text=f"{self.character if self.character else 'Character Sheet'}", justify=tk.CENTER , anchor=tk.CENTER)
        self.fullname_label.pack(pady=5, padx=10, anchor=tk.W)

        self.age_label = ttk.Label(self.info_frame, text=f"Age: {self.character.age if self.character else 'N/A'}")
        self.age_label.pack(pady=5, padx=10, anchor=tk.W)

        self.generation_label = ttk.Label(self.info_frame, text=f"Generation: {self.character.generation if self.character else 'N/A'}")
        self.generation_label.pack(pady=5, padx=10, anchor=tk.W)

        self.lineage_label = ttk.Label(self.info_frame, text=f"Lineage: {self.character.lineage if self.character else 'N/A'}")
        self.lineage_label.pack(pady=5, padx=10, anchor=tk.W)

        self.job_label = ttk.Label(self.info_frame, text=f"Job: {self.character.job if self.character else 'N/A'}")
        self.job_label.pack(pady=5, padx=10, anchor=tk.W)

        self.titles_label = ttk.Label(self.info_frame, text=f"Titles: {', '.join(self.character.titles) if self.character else 'N/A'}")
        self.titles_label.pack(pady=5, padx=10, anchor=tk.W)

        if self.character and hasattr(self.character, 'picture') and self.character.picture:
            self.display_character_image(self.character.picture)






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
    
    def display_character_image(self, image_path):
        try:
            image = Image.open(image_path)
            self.update_idletasks()
            frame_width = self.winfo_width()
            frame_height = self.winfo_height()
            aspect_ratio = image.width / image.height
            new_width = min(frame_width, (int(frame_height * aspect_ratio)))
            new_height = min(frame_height, (int(frame_width / aspect_ratio)))
            image = image.resize((400, new_height))
            self.character_image = ImageTk.PhotoImage(image)
            self.image_label = ttk.Label(self.picture_frame, image=self.character_image, anchor=tk.CENTER, justify=tk.CENTER)
            self.image_label.place(in_=self.picture_frame, relx=0.5, rely=0.5, anchor=tk.CENTER)
        except Exception as e:
            print(f"Erreur lors du chargement de l'image : {e}")