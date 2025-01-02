import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from models import create_complete_menu, Customer
from gestione import register_user, login_user
from immagini import load_images


# Finestra di Menu
class MenuApp:
    def __init__(self, root, customer=None):
        self.root = root
        self.root.title("STALLIONS MENU'")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f2e6d9")

        self.menu = create_complete_menu()  # Assicurati che il menu venga caricato correttamente
        self.images = load_images()  # Carica le immagini dei piatti
        self.current_order = []  # Lista per tenere traccia dei piatti selezionati
        self.order_quantities = {}  # Dizionario per tenere traccia delle quantità degli ordini
        self.customer = customer  # Cliente loggato

        self.create_widgets()

    def create_widgets(self):
        try:
            self.logo_image = tk.PhotoImage(file="stallone.png")  # Assicurati che il percorso dell'immagine sia corretto
            self.logo_label = tk.Label(self.root, image=self.logo_image, bg="#f2e6d9")
            self.logo_label.pack(pady=20)  # Aggiungi il logo sopra il titolo
        except Exception as e:
            print(f"Errore nel caricare l'immagine del logo: {e}")

        self.title_label = tk.Label(self.root, text="STALLIONS MENU", font=("Courier New", 28, "bold"), bg="#8b4513", fg="#fff")
        self.title_label.pack(fill="x", pady=10)

        self.menu_canvas = tk.Canvas(self.root, bg="#f2e6d9", highlightthickness=0)
        self.menu_scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.menu_canvas.yview)
        self.menu_frame = tk.Frame(self.menu_canvas, bg="#f2e6d9")

        self.menu_frame.bind(
            "<Configure>",
            lambda e: self.menu_canvas.configure(scrollregion=self.menu_canvas.bbox("all"))
        )
        self.menu_canvas.create_window((0, 0), window=self.menu_frame, anchor="nw")
        self.menu_canvas.configure(yscrollcommand=self.menu_scrollbar.set)

        self.menu_canvas.pack(side="left", fill="both", expand=True, pady=10)
        self.menu_scrollbar.pack(side="right", fill="y")

        self.menu_canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)

        self.create_menu_buttons()

        self.summary_button = tk.Button(self.root, text="Mostra Ordine", command=self.show_order_summary,
                                        font=("Courier New", 12), bg="#e67e22", fg="#fff")
        self.summary_button.pack(pady=10)

        self.total_button = tk.Button(self.root, text="Mostra Totale (IVA Inclusa)", command=self.show_total,
                                      font=("Courier New", 12), bg="#e67e22", fg="#fff")
        self.total_button.pack(pady=10)

        self.delete_button = tk.Button(self.root, text="Elimina Ordini Selezionati", command=self.delete_selected_orders,
                                       font=("Courier New", 12), bg="#e67e22", fg="#fff")
        self.delete_button.pack(pady=10)

        if self.customer:
            user_label = tk.Label(self.root, text=f"Benvenuto, {self.customer.username}!", font=("Courier New", 14, "bold"), bg="#f2e6d9")
            user_label.pack(pady=10)

    def create_menu_buttons(self):
        for category, items in self.menu.items.items():
            category_label = tk.Label(self.menu_frame, text=category, font=("Courier New", 18, "bold"), bg="#f2e6d9", fg="#8b4513")
            category_label.pack(anchor="w", pady=(10, 0))

            frame = tk.Frame(self.menu_frame, bg="#f2e6d9")
            frame.pack(anchor="w")

            for item in items:
                image = self.images.get(item.name)
                button = tk.Button(frame, text=f"{item.name} - {item.price}€", image=image, compound="left",
                                   command=lambda i=item: self.add_item_to_order(i),
                                   font=("Courier New", 12), bg="#e67e22", fg="#fff")
                button.pack(side="left", padx=5, pady=5)
                button.image = image

    def add_item_to_order(self, item):
        # Aggiungi o aggiorna la quantità dell'item
        if item.name in self.order_quantities:
            self.order_quantities[item.name] += 1
        else:
            self.order_quantities[item.name] = 1
        
        # Aggiungi l'item alla lista dell'ordine
        self.current_order.append(item)

    def show_order_summary(self):
        summary_window = tk.Toplevel(self.root)
        summary_window.title("Riepilogo Ordine")
        summary_window.geometry("400x600")
        summary_window.configure(bg="#f2e6d9")

        summary_label = tk.Label(summary_window, text="Riepilogo Ordine", font=("Courier New", 18, "bold"), bg="#8b4513", fg="#fff")
        summary_label.pack(fill="x", pady=10)

        order_text = ""
        for item in self.order_quantities:
            quantity = self.order_quantities[item]
            order_text += f"{item} - {quantity}x\n"  # Formato come 'item x2'
        
        order_label = tk.Label(summary_window, text=order_text, font=("Courier New", 12), bg="#f2e6d9", fg="#8b4513")
        order_label.pack(pady=10)

    def show_total(self):
        total_window = tk.Toplevel(self.root)
        total_window.title("Totale con IVA")
        total_window.geometry("300x200")
        total_window.configure(bg="#f2e6d9")

        total = sum(item.price for item in self.current_order)
        iva = total * 0.22
        total_with_iva = total + iva

        total_label = tk.Label(total_window, text=f"Totale: {total:.2f}€\nIVA (22%): {iva:.2f}€\nTotale con IVA: {total_with_iva:.2f}€",
                               font=("Courier New", 14), bg="#f2e6d9", fg="#8b4513")
        total_label.pack(pady=20)

    def delete_selected_orders(self):
        if not self.current_order:
            messagebox.showerror("Errore", "Non ci sono ordini da eliminare.")
            return

        delete_window = tk.Toplevel(self.root)
        delete_window.title("Elimina Ordini Selezionati")
        delete_window.geometry("400x400")
        delete_window.configure(bg="#f2e6d9")

        delete_label = tk.Label(delete_window, text="Seleziona uno o più ordini da eliminare", font=("Courier New", 16, "bold"), bg="#8b4513", fg="#fff")
        delete_label.pack(pady=10)

        order_listbox = tk.Listbox(delete_window, height=10, width=40, font=("Courier New", 12), selectmode="multiple")
        for index, item in enumerate(self.current_order):
            order_listbox.insert(tk.END, f"{index+1}. {item.name} - {item.price}€")
        order_listbox.pack(pady=10)

        def confirm_deletion():
            selected_indices = order_listbox.curselection()
            if not selected_indices:
                messagebox.showerror("Errore", "Seleziona almeno un ordine da eliminare.")
                return

            items_to_remove = [self.current_order[i] for i in selected_indices]
            for item in items_to_remove:
                self.current_order.remove(item)

            messagebox.showinfo("Ordini Eliminati", f"{len(items_to_remove)} ordini sono stati eliminati con successo.")
            delete_window.destroy()

        delete_button = tk.Button(delete_window, text="Elimina Ordini Selezionati", command=confirm_deletion,
                                  font=("Courier New", 12), bg="#e67e22", fg="#fff")
        delete_button.pack(pady=10)

    def on_mouse_wheel(self, event):
        if event.delta > 0:
            self.menu_canvas.yview_scroll(-1, "units")
        else:
            self.menu_canvas.yview_scroll(1, "units")


# Finestra di Login
class AuthWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login / Registrazione")
        self.root.geometry("400x300")
        self.root.configure(bg="#f2e6d9")

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Login / Registrazione", font=("Courier New", 20, "bold"), bg="#8b4513", fg="#fff")
        self.title_label.pack(pady=20)

        self.username_label = tk.Label(self.root, text="Username:", font=("Courier New", 12), bg="#f2e6d9")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.root, font=("Courier New", 12))
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self.root, text="Password:", font=("Courier New", 12), bg="#f2e6d9")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root, font=("Courier New", 12), show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self.root, text="Login", command=self.login, font=("Courier New", 12), bg="#e67e22", fg="#fff")
        self.login_button.pack(pady=10)

        self.register_button = tk.Button(self.root, text="Registrati", command=self.register, font=("Courier New", 12), bg="#e67e22", fg="#fff")
        self.register_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        customer = login_user(username, password)
        if customer:
            messagebox.showinfo("Login", "Login effettuato con successo!")
            self.root.destroy()

            # Passa il cliente alla finestra del menu
            root = tk.Tk()
            app = MenuApp(root, customer=customer)
            root.mainloop()
        else:
            messagebox.showerror("Errore", "Credenziali errate. Riprova.")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if register_user(username, password):
            messagebox.showinfo("Registrazione", "Registrazione avvenuta con successo!")
        else:
            messagebox.showerror("Errore", "Errore durante la registrazione.")


# Main execution
def start_app():
    root = tk.Tk()
    app = AuthWindow(root)
    root.mainloop()


if __name__ == "__main__":
    start_app()
