from src.gui.main import App 
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gentree")
    root.geometry("800x600")
    app = App(root)
    root.mainloop()