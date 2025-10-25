def main(model_type, quantity):
    prices = {
        "laptop": 900,
        "desktop": 1200,
        "workstation": 2000,
        "mini_pc": 700
    }
    total = prices[model_type] * quantity
    return f"${total}"
