# -----> File: compare_cars.py <-----
def main(car1, car2):
    # Define car features and prices
    cars = {
        "Bugatti": {"price": 2500000, "features": "Quad-turbocharged W16 engine, all-wheel drive, top speed over 300 mph"},
        "Ferrari": {"price": 215000, "features": "V8 engine, advanced aerodynamics, luxurious interior"},
        "Pagani": {"price": 2600000, "features": "Lightweight carbon-titanium structure, AMG V12 engine"},
        "McLaren": {"price": 210000, "features": "Lightweight chassis, twin-turbo V8 engine"},
        "Koenigsegg": {"price": 3000000, "features": "Lightweight carbon fiber body, advanced aerodynamics"},
    }

    # Get the details of the selected cars
    car1_details = cars[car1]
    car2_details = cars[car2]

    # Create comparison result
    result = f"{car1} - Price: ${car1_details['price']}, Features: {car1_details['features']}\n" \
             f"{car2} - Price: ${car2_details['price']}, Features: {car2_details['features']}"

    return result