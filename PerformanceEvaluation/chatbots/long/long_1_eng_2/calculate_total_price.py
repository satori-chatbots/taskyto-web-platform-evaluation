def main(dogs_quantity, cats_quantity, rabbits_quantity, hamsters_quantity):
    prices = {
        'dogs': 400,
        'cats': 250,
        'rabbits': 125,
        'hamsters': 100
    }
    
    total_price = (dogs_quantity or 0) * prices['dogs'] + \
                  (cats_quantity or 0) * prices['cats'] + \
                  (rabbits_quantity or 0) * prices['rabbits'] + \
                  (hamsters_quantity or 0) * prices['hamsters']
    
    return str(total_price)