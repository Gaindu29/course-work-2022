def for_srr():
    import random
    import datetime

    # getting a random date for the race
    d = random.randint(1, 10)
    m = random.randint(1, 1)
    y = random.randint(2023, 2023)
    format_date = datetime.date(y, m, d)
    date = str(format_date)

    # getting a random Location
    locations = ["Nyirad", "Holjes", "Montalegre", "Barcelona", "Riga", "Norway"]
    random_location = random.choice(locations)

    race_date = open("date_location.txt", "a+")
    race_date.write(date + " , " + random_location + "\n")
    race_date.close()

    drivers = []
    with open("driver_details.txt") as file1:
        file2 = file1.readlines()
    file1.close()

    count = 0
    # adding driver details into the list
    for i in file2:
        x = i.replace("[", "").replace("]", "").replace(" ", "").replace("\"", "").replace("\'", "").\
            replace("\n", "").strip().split(",")
        drivers.append(x)
        count += 1

    # get races in random order
    random.shuffle(drivers)

    # get a position for the shuffled races
    positions = []
    for i in range(1, count + 1):
        positions.append(i)

    # to add driver details with position into a list
    driver_position = []
    count = 0
    for i in drivers:
        driver = [positions[count]]
        for n in i:
            driver .append(n)
        driver_position.append(driver)
        count += 1

    # stores updated points
    update_positions = []

    # call driver name one at a time to update
    for driver in driver_position:
        update_points = []
        for detail in driver:
            if count == 5:

                # adding points to driver position first
                if driver[0] == 1:
                    points = int(driver[5]) + 10
                    update_points.append(points)
                    break

                # adding points to driver position second
                elif driver[0] == 2:
                    points = int(driver[5]) + 7
                    update_points.append(points)
                    break

                # adding points to driver position third
                elif driver[0] == 3:
                    points = int(driver[5]) + 5
                    update_points.append(points)
                    break

                else:
                    update_points.append(detail)
                    break

            elif count != 5:
                update_points.append(detail)

            count += 1

        update_positions.append(update_points)

    #  save the updated points to a list
    random_positions = open("random.txt", "a+")

    random_positions.write("Date\t:\t" + str(date) + "  \t\t, Location\t:\t" + random_location + "\n")
    for x in update_positions:
        random_positions.write(str(x) + "\n")
    random_positions.close()

    date_file = open("date_order.txt", "a+")
    date_file.write(date + "," + random_location)
    date_file.close()

    print("\nThe data has been saved")

    view = int(input("\npress 1 to view the data : "))

    if view == 1:
        # to display race detail
        po_file = open("random.txt", "r")
        for x in po_file:
            x = x.replace("[", "").replace("]", "").replace(" ", "").replace("\"", "").replace("\'", ""). \
                replace("\n", "").strip().split(",")
            for y in x:
                print(y, "\t", end="")
            print("\n")







