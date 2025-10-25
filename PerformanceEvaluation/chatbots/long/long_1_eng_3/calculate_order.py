def main(dogs, cats, rabbits, hamsters, appointment_date):
    prices = {
        'dogs': 400,
        'cats': 250,
        'rabbits': 125,
        'hamsters': 100
    }
    
    total_price = 0
    if dogs:
        total_price += min(dogs, 5) * prices['dogs']
    if cats:
        total_price += min(cats, 5) * prices['cats']
    if rabbits:
        total_price += min(rabbits, 5) * prices['rabbits']
    if hamsters:
        total_price += min(hamsters, 5) * prices['hamsters']
    
    return f"${total_price}"