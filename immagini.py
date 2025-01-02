import os
from tkinter import PhotoImage

def load_images():
    images = {}
    path = os.path.join(os.path.dirname(__file__), "images")
    for file in os.listdir(path):
        if file.endswith(".png"):
            name = file.replace(".png", "").replace("_", " ").title()
            full_path = os.path.join(path, file)
            try:
                images[name] = PhotoImage(file=full_path)
            except Exception as e:
                print(f"Errore nel caricamento di {file}: {e}")
    return images