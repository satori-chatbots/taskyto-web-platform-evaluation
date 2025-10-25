def main(dogs, cats, rabbits, hamsters):
    total_cost = 0
    if dogs:
        total_cost += dogs * 400
    if cats:
        total_cost += cats * 250
    if rabbits:
        total_cost += rabbits * 125
    if hamsters:
        total_cost += hamsters * 100

    return f"Your total order cost is ${total_cost}."
