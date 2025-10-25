def main(check_in_date, check_out_date, room_type, number_of_rooms):
    # Define room prices
    prices = {
        "standard": 80,
        "double": 120,
        "suite": 200
    }
    
    # Calculate the number of nights
    nights = (check_out_date - check_in_date).days
    
    # Calculate total cost
    total_cost = nights * prices[room_type] * number_of_rooms
    return str(total_cost)
