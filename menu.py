import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from gestione import register_user, login_user, Customer

class MenuApp:
    def __init__(self, root, customer=None):
        self.root = root
        self.root.title("Stallions Menu")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f2e6d9")

        self.current_order = []  # Lista per tenere traccia dei piatti selezionati
        self.customer = customer  # Cliente loggato

        self.create_widgets()

    def create_widgets(self):
        # Titolo della finestra
        self.title_label = tk.Label(self.root, text="STALLIONS MENU", font=("Courier New", 28, "bold"), bg="#8b4513", fg="#fff")
        self.title_label.pack(fill="x", pady=10)

        # Visualizza il nome dell'utente
        if self.customer:
            user_label = tk.Label(self.root, text=f"Benvenuto, {self.customer.username}!", font=("Courier New", 14, "bold"), bg="#f2e6d9")
            user_label.pack(pady=10)

        # Aggiungi bottoni per l'ordine e altre funzionalità
        self.summary_button = tk.Button(self.root, text="Mostra Ordine", command=self.show_order_summary,
                                        font=("Courier New", 12), bg="#e67e22", fg="#fff")
        self.summary_button.pack(pady=10)

        self.total_button = tk.Button(self.root, text="Mostra Totale (IVA Inclusa)", command=self.show_total,
                                      font=("Courier New", 12), bg="#e67e22", fg="#fff")
        self.total_button.pack(pady=10)

    def show_order_summary(self):
        summary_window = tk.Toplevel(self.root)
        summary_window.title("Riepilogo Ordine")
        summary_window.geometry("400x600")
        summary_window.configure(bg="#f2e6d9")

        summary_label = tk.Label(summary_window, text="Riepilogo Ordine", font=("Courier New", 18, "bold"), bg="#8b4513", fg="#fff")
        summary_label.pack(fill="x", pady=10)

    def show_total(self):
        total_window = tk.Toplevel(self.root)
        total_window.title("Totale con IVA")
        total_window.geometry("300x200")
        total_window.configure(bg="#f2e6d9")

        total_label = tk.Label(total_window, text="Totale: 50.00€", font=("Courier New", 14), bg="#f2e6d9", fg="#8b4513")
        total_label.pack(pady=20)
