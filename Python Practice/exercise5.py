menu = { "Pizza": 1.99, "Soda":  0.69, "Double Chunk Chocolate Chip Cookie": 2.49}

def add_menu_item(item, price):
    menu[item] = price
    print(menu)

add_menu_item("Chicken Bake", 4.00)