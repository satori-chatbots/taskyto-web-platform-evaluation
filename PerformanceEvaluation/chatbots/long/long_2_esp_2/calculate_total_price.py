def main(pickup_date, computer_type, quantity):
    prices = {
        "laptop": 900,
        "desktop": 1200,
        "workstation": 2000,
        "mini_pc": 700
    }
    total_price = prices[computer_type] * quantity
    return f"${total_price}"
