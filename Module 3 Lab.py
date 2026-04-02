class Ride:
    def __init__(self, ride_type):
        self.ride_type = ride_type
class Automobile(Ride):
    def __init__(self, ride_type, year, make, model, doors, roof):
        super().__init__(ride_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
def main():
    print("--- Vehicle Data Entry ---")
    v_type = "car"
    year = input("year?: ")
    make = input("make?: ")
    model = input("model?: ")
    doors = input("doors?: ")
    roof = input("roof?: ")
    user_car = Automobile(v_type, year, make, model, doors, roof)
    print("\n--- Vehicle Information ---")
    print(f"Ride type: {user_car.ride_type}")
    print(f"Year: {user_car.year}")
    print(f"Make: {user_car.make}")
    print(f"Model: {user_car.model}")
    print(f"Number of doors: {user_car.doors}")
    print(f"Type of roof: {user_car.roof}")
if __name__ == "__main__":
    main()