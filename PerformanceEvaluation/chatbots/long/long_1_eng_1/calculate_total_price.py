def main(dogs, cats, rabbits, hamsters):
    prices = {
        'dogs': 400,
        'cats': 250,
        'rabbits': 125,
        'hamsters': 100
    }
    
    total_price = (dogs * prices['dogs'] if dogs else 0) + \
                  (cats * prices['cats'] if cats else 0) + \
                  (rabbits * prices['rabbits'] if rabbits else 0) + \
                  (hamsters * prices['hamsters'] if hamsters else 0)
    
    return str(total_price)