def main(check_in_date, check_out_date, room_type, number_of_rooms):
    prices = {
        "estándar": 80,
        "doble": 120,
        "suite": 200
    }
    
    # Calculate the number of nights
    from datetime import datetime
    check_in = datetime.strptime(check_in_date, "%Y-%m-%d")
    check_out = datetime.strptime(check_out_date, "%Y-%m-%d")
    number_of_nights = (check_out - check_in).days
    
    # Calculate total cost
    total_cost = prices[room_type] * number_of_rooms * number_of_nights
    return f"${total_cost}"
