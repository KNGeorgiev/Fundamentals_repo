car_number = int(input())
car_dict = {}

for x in range(car_number):
    car_data = input().split("|")
    car = car_data[0]
    mileage = int(car_data[1])
    fuel = int(car_data[2])
    car_dict[car] = {"mileage": mileage, "fuel": fuel}

while True:
    command = input().split(" : ")

    if command[0] == "Stop":
        for car in car_dict:
            print(f"{car} -> Mileage: {car_dict[car]['mileage']} kms, Fuel in the tank: {car_dict[car]['fuel']} lt.")
        break

    elif command[0] == "Drive":
        car = command[1]
        distance = int(command[2])
        needed_fuel = int(command[3])
        if needed_fuel > car_dict[car]["fuel"]:
            print("Not enough fuel to make that ride")
        else:
            car_dict[car]["mileage"] += distance
            car_dict[car]["fuel"] -= needed_fuel
            print(f"{car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
        if car_dict[car]["mileage"] >= 100000:
            del car_dict[car]
            print(f"Time to sell the {car}!")

    elif command[0] == "Refuel":
        car = command[1]
        refuel = int(command[2])
        needed_refuel = 75 - car_dict[car]["fuel"]
        if refuel <= needed_refuel:
            car_dict[car]["fuel"] += refuel
            print(f"{car} refueled with {refuel} liters")
        else:
            car_dict[car]["fuel"] = 75
            print(f"{car} refueled with {needed_refuel} liters")

    elif command[0] == "Revert":
        car = command[1]
        kilometers = int(command[2])
        kilometers_difference = car_dict[car]["mileage"] - kilometers
        if kilometers_difference >= 10000:
            car_dict[car]["mileage"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            car_dict[car]["mileage"] = 10000
