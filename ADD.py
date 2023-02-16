def for_add():  # used to enter the user details

    # to read the file from the driver file

    driver_details = []
    name = str(input("\nPlease enter your full name : "))  # getting name
    driver_details.append(name)

    while True:  # verifying age making sure it's an integer
        try:
            age = int(input("\nPlease enter your age : "))
            driver_details.append(age)
            break
        except:
            print("invalid age")
            continue

    team = str(input("\nPlease enter the team name : "))  # getting team name
    driver_details.append(team)

    car = str(input("\nPlease enter your car model : "))  # getting car model
    driver_details.append(car)

    while True:  # verifying current points making sure it's an integer
        try:
            current_points = int(input("\nPlease enter the amount of current points you have : "))
            driver_details.append(current_points)
            break
        except:
            print("invalid points value")
            continue

    print(
        "\nYou have sucessfully entered the details")  # adding the values so that they get entered in rows
    details = open("driver_details.txt", "a+")
    details.writelines(str(driver_details) + "\n")
    details.close()

    details = open("driver_details.txt", "r")  # printing the entered values for the user
    contents = details.read()
    print(contents)
    details.close()


