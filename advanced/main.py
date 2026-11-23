
robot = {
    "name": "leenieeee",
    "model": "leniez-67bot",
    "battery": 67,
    "speed": 6.7,
    "mode": "cutesieness"
}

while True:
    print("\n===== LEENIEEEE'S ROBOT EMPIRE =====")
    print("1. View all my settings")
    print("2. Look up a setting")
    print("3. Change a setting")
    print("4. add a setting")
    print("5. Exit")

    choice = input("Enter your choice, your majesty: ")

    if choice == "1":
        print("\n===== THE QUEEN'S ROBOT SETTINGS =====")

        for key, value in robot.items():
            print(key, ":", value)

    elif choice == "2":
        key = input("What setting are we looking for?!?? ")

        value = robot.get(key)

        if value is not None:
            print(key, ":", value)
        else:
            print("HELLO??? That setting does not exist.")

    elif choice == "3":
        key = input("What setting are we changing today? ")

        if key in robot:
            new_value = input("Enter the new value: ")
            robot[key] = new_value

            print("PERIOD. Setting updated ':!")

        else:
            print("That setting does not exist??. Try again.!!")

    elif choice == "4":
        key = input("What new setting are we adding? ")

        if key not in robot:
            value = input("Enter its value: ")
            robot[key] = value

            print("New setting added. The empire grows!")

        else:
            print("son, that setting already exists.")

    elif choice == "5":
        print("Goodbye! quandledingle has left the empire.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
