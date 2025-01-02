# models.py

class Menu:
    def __init__(self):
        self.items = {
            "Antipasti": [
                {"name": "Tagliere di Salumi", "price": 15},
                {"name": "Classic", "price": 10}
            ],
            "Primi": [
                {"name": "Trofie ai Funghi", "price": 12}
            ],
            "Secondi": [
                {"name": "Tagliata di Manzo", "price": 20},
                {"name": "Filetto al Pepe Verde", "price": 25},
                {"name": "Tagliata Black Angus", "price": 28},
                {"name": "Filetto Kobe", "price": 45}
            ],
            "Hamburger": [
                {"name": "American Burger", "price": 13},
                {"name": "Stallions Burger", "price": 15}
            ],
            "Contorni": [
                {"name": "Patatine Fritte", "price": 5},
                {"name": "Insalata Mista", "price": 6},
                {"name": "Verdure Grigliate", "price": 7},
                {"name": "Special Fries", "price": 6}
            ],
            "Dolci": [
                {"name": "Tiramisu", "price": 7},
                {"name": "Cheesecake", "price": 8},
                {"name": "Babà", "price": 6}
            ],
            "Bevande": [
                {"name": "Acqua Naturale", "price": 2},
                {"name": "Coca Cola", "price": 3},
                {"name": "Chianti Classico", "price": 20},
                {"name": "Birra Spina", "price": 4},
                {"name": "Brunello di Montalcino", "price": 30}
            ]
        }

class Order:
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        
    def get_summary(self):
        summary = ""
        for item in self.items:
            summary += f"{item['name']} - {item['price']}€\n"
        return summary


class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.orders = []

    def create_order(self):
        return Order()

    def get_order_summary(self):
        summary = ""
        for order in self.orders:
            summary += order.get_summary() + "\n"
        return summary

