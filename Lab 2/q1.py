class Vehicle:
    vehicle_id=0
    brand=""
    rent_per_day=0
    def __init__ (self,vehicle_id,brand,rent_per_day):
        self.vehicle_id=vehicle_id
        self.brand=brand
        self.rent_per_day=rent_per_day
    def display_details(self):
        print(f"Vehicle Id : {self.vehicle_id}, Brand : {self.brand}, Rent per day : {self.rent_per_day}")
    def calculate_rent(self,days):
        print("Rent is : ", self.rent_per_day*days ,"for", days, "days")

vehicle1=Vehicle(695,"Toyota",670)
vehicle2=Vehicle(644,"Hyundai",900)

print("Vehicle 1 : ")
vehicle1.display_details()
vehicle1.calculate_rent(4)
vehicle1.calculate_rent(10)

print("\nVehicle 2 : ")
vehicle2.display_details()
vehicle2.calculate_rent(7)
vehicle2.calculate_rent(11)
