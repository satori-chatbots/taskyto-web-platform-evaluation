def main(pickup_date, computers, quantities):
    prices = {
        "laptops": 900,
        "desktops": 1200,
        "workstations": 2000,
        "mini PCs": 700
    }
    total_price = prices[computers] * quantities
    return f"${total_price}"
