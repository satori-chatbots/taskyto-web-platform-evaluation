def main(name, email, phone_number, check_in, check_out, room_type):
    # Here you would typically save the reservation to a database or send a confirmation email
    print(f"Reservation confirmed for {name} in a {room_type} from {check_in} to {check_out}.")
    return "Reservation confirmed successfully!"

# Ensure to call the main function and return its value
result = main(name, email, phone_number, check_in, check_out, room_type)