from parked_car import ParkedCar
from parking_meter import ParkingMeter
from police_officer import PoliceOfficer

def scenario_1():
    print("\n--- Scenario 1: Car Parked Legally ---")
    car = ParkedCar("Toyota", "Camry", "Red", "XYZ123", minutes_parked=30)
    meter = ParkingMeter(minutes_purchased=40)
    officer = PoliceOfficer("John Doe", "5678")
    ticket = officer.inspect_car(car, meter)
    if ticket:
        print(ticket)
    else:
        print("No ticket issued: car is legally parked.")

def scenario_2():
    print("\n--- Scenario 2: Car Illegally Parked (< 1 hour over) ---")
    car = ParkedCar("Honda", "Accord", "Blue", "ABC987", minutes_parked=70)
    meter = ParkingMeter(minutes_purchased=60)
    officer = PoliceOfficer("Jane Smith", "1234")
    ticket = officer.inspect_car(car, meter)
    print(ticket if ticket else "No ticket issued")

def scenario_3():
    print("\n--- Scenario 3: Car Illegally Parked (Multiple hours over) ---")
    car = ParkedCar("Ford", "Mustang", "Black", "LMN456", minutes_parked=190)
    meter = ParkingMeter(minutes_purchased=60)
    officer = PoliceOfficer("James Brown", "4321")
    ticket = officer.inspect_car(car, meter)
    print(ticket if ticket else "No ticket issued")

def scenario_4():
    print("\n--- Scenario 4: Multiple Cars in a Lot ---")
    officer = PoliceOfficer("Sarah Green", "9999")
    dataset = [
        ("Nissan", "Altima", "White", "JKL321", 60, 60),
        ("Chevy", "Malibu", "Silver", "QWE789", 80, 60),
        ("BMW", "X5", "Black", "BMW999", 500, 60),
        ("Mazda", "3", "Blue", "MAZ321", 45, 60),
        ("Hyundai", "Elantra", "Grey", "HYU123", 65, 60),
    ]
    for rec in dataset:
        car = ParkedCar(rec[0], rec[1], rec[2], rec[3], minutes_parked=rec[4])
        meter = ParkingMeter(minutes_purchased=rec[5])
        ticket = officer.inspect_car(car, meter)
        print(ticket if ticket else f"No ticket: {car}")

if __name__ == "__main__":
    scenario_1()
    scenario_2()
    scenario_3()
    scenario_4()