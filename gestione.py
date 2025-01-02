from models import Customer, save_customer, load_customers

# Funzione per registrare un nuovo utente
def register_user(username, password):
    customers = load_customers()
    
    # Controlla se l'username è già preso
    if username in customers:
        print("Username già esistente. Scegli un altro nome utente.")
        return False
    
    # Crea un nuovo cliente
    customer = Customer(username, password)
    
    # Salva il cliente nel file JSON
    save_customer(customer)
    print(f"Utente {username} registrato con successo!")
    return True

# Funzione per fare il login di un utente
def login_user(username, password):
    customers = load_customers()
    
    # Verifica se l'utente esiste e la password corrisponde
    if username in customers and customers[username]["password"] == password:
        return Customer(username, password)
    
    # Se le credenziali sono errate
    return None
