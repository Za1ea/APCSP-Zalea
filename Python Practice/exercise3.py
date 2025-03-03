groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]

while True:
    item = input(f"What item do you want to remove from this grocery list: {groceries}\n If you don't want to remove any item, type 'stop'.\n")
    if item.lower() == "stop":
        break
    groceries.remove(item)