class BMW:
    def fuel_type(self):
        print("BMW fuel type is Petrol")

    def max_speed(self):
        print("BMW max speed is 250 kmh")


class Ferrari:
    def fuel_type(self):
        print("Ferrari fuel type is Premium Petrol")

    def max_speed(self):
        print("Ferrari max speed is 340 kmh")

# Create class instances
car_bmw = BMW()
car_ferrari = Ferrari()

for car in (car_bmw, car_ferrari):
    car.fuel_type()
    car.max_speed()
