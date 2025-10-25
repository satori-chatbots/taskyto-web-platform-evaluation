def main(dogs_count, cats_count, rabbits_count, hamsters_count):
    prices = {
        'dog': 400,
        'cat': 250,
        'rabbit': 125,
        'hamster': 100
    }
    
    total_price = 0
    if dogs_count:
        total_price += dogs_count * prices['dog']
    if cats_count:
        total_price += cats_count * prices['cat']
    if rabbits_count:
        total_price += rabbits_count * prices['rabbit']
    if hamsters_count:
        total_price += hamsters_count * prices['hamster']
    
    return str(total_price)