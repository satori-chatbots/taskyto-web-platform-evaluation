def main(dogs, cats, rabbits, hamsters):
    prices = {
        "dogs": 400,
        "cats": 250,
        "rabbits": 125,
        "hamsters": 100
    }
    
    total_cost = (dogs * prices["dogs"]) + (cats * prices["cats"]) + (rabbits * prices["rabbits"]) + (hamsters * prices["hamsters"])
    
    return f"Total cost for your order is ${total_cost}."
