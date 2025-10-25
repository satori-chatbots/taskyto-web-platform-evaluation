def main(check_in_date, check_out_date, room_type, number_of_rooms):
    # Logic to make a reservation
    total_cost = number_of_rooms * (80 if room_type == "standard" else 120 if room_type == "double" else 200)
    return f"Reservation confirmed! Total cost is ${total_cost}."