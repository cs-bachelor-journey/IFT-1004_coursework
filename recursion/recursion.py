catalog = {
    "electronics": {
        "laptops": {
            "ThinkPad X1": 1299.99,
            "MacBook Air": 1099.99
        },
        "accessories": {
            "USB-C Hub": 49.99,
            "Laptop Stand": 34.99
        }
    },
    "stationery": {
        "Notebook A5": 8.99,
        "Gel Pen Set": 12.49
    }
}

def find_all_prices(data):
    prices = []
    
    for value in data.values():
        if isinstance(value, dict):
            # It's a nested dict - recurse into it
            prices.extend(find_all_prices(value))
        else:
            # It's a price - collect it
            prices.append(value)
    
    return prices

all_prices = find_all_prices(catalog)
print(f"All prices: {all_prices}")
print(f"Total inventory value: ${sum(all_prices):.2f}")