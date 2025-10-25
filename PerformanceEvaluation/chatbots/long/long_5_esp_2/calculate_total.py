def main(check_in, check_out, room_type, number_of_rooms):
    # Define room prices
    prices = {
        "estándar": 80,
        "doble": 120,
        "suite": 200
    }
    
    # Calculate number of nights
    from datetime import datetime
    check_in_date = datetime.strptime(check_in, '%Y-%m-%d')
    check_out_date = datetime.strptime(check_out, '%Y-%m-%d')
    number_of_nights = (check_out_date - check_in_date).days
    
    # Calculate total
    total = number_of_nights * prices[room_type] * number_of_rooms
    return str(total)
