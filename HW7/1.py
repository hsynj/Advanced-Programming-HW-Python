class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = False


    def display_info(self):
        print("---------------------------")
        print("Car Information:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Created in {self.year}")
        print(f"Engine status: {'Running' if self.engine else 'Off'}")


    def start_engine(self):
        print(f"-> The engine of the {self.brand} {self.model} is now running.")
        self.engine = True


    def stop_engine(self):
        print(f"-> The engine of the {self.brand} {self.model} is now off.")
        self.engine = False


    def __str__(self):
        return f"The {self.brand} {self.model} as {self.year} is {'Running' if self.engine else 'Off'}."
    

    def __repr__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Engine: {'Running' if self.engine else 'Off'}"


# Example usage
my_car = Car("Tesla", "Model 5", 2023)
my_car.display_info()
my_car.start_engine()
my_car.display_info()
my_car.stop_engine()
my_car.display_info()

print(my_car)
print(repr(my_car))
