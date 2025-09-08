class Vehicle:
    
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
obj = Vehicle(240, 18)

print("Model's Max Speed: ", obj.max_speed)
print("Model's Mileage: ", obj.mileage)
