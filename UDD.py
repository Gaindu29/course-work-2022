def for_udd():  # update driver details

    # removing the driver so the updated details can be entered
    name_alter = input("\nEnter the name of the driver whose details should be updated : ")

    # removing the previous details
    with open("driver_details.txt", "r") as fileR:
        with open("tempfile.txt", "w") as fileW:
            x = fileR.readlines()
            for i in x:
                value = i.replace("[", "").replace("]", "").replace("\"", "").replace("\'", "").replace("\n", "").split(
                    ", ")
                if name_alter != value[0]:
                    fileW.write(str(i))

        fileW.close()
    fileR.close()

    # copying data back to driver_details
    with open("tempfile.txt", "r") as file:
        with open("driver_details.txt", "w") as fileW:
            for value in file:
                fileW.write(str(value))

    # getting name
    driver_details = []
    name = str(input("\nPlease enter your full name : "))
    driver_details.append(name)

    # verifying age making sure it's an integer
    while True:
        try:
            age = int(input("\nPlease enter your age : "))
            driver_details.append(age)
            break
        except :
            print("invalid age")
            continue

    # getting team name
    team = str(input("Please enter the team name : "))
    driver_details.append(team)

    # getting car model
    car = str(input("Please enter your car model : "))
    driver_details.append(car)

    # verifying current points making sure it's an integer
    while True:
        try:
            current_points = int(input("Please enter the amount of current points you have : "))
            driver_details.append(current_points)
            break
        except:
            print("invalid points value")
            continue

    # adding the values so that they get entered in rows
    print(
        "\nYou have sucessfully entered the details")

    details = open("driver_details.txt", "a+")
    details.writelines(str(driver_details) + "\n")
    details.close()

    # printing the entered values for the user
    details = open("driver_details.txt", "r")
    contents = details.read()
    print(contents)
    details.close()