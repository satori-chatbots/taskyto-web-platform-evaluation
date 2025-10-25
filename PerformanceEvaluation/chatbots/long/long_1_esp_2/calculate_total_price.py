def main(dogs, cats, rabbits, hamsters):
    prices = {
        'dogs': 400,
        'cats': 250,
        'rabbits': 125,
        'hamsters': 100
    }
    
    total = 0
    if dogs:
        total += dogs * prices['dogs']
    if cats:
        total += cats * prices['cats']
    if rabbits:
        total += rabbits * prices['rabbits']
    if hamsters:
        total += hamsters * prices['hamsters']
    
    return str(total)