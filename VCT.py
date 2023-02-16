def for_vct():
    details = open("driver_details.txt", "r")
    file1 = details.readlines()
    details.close()

    current_points = []
    # stores all the current points in a list
    for line in file1:
        i = line.replace("[", "").replace("]", "").replace("\"", "").replace("\'", "").replace("\n", "").strip().split(
            ",")
        current_points.append(int(i[-1]))

    dec_order = []
    # sorts the current points and stores them
    while current_points:
        points_descending = current_points[0]

        for x in current_points:
            if x > points_descending:
                points_descending = x

        dec_order.append(points_descending)
        current_points.remove(points_descending)

    temp = open("sort_desc.txt", "w")
    for y in dec_order:
        for line in file1:
            x = line.replace("[", "").replace("]", "").replace("\"", "").replace("\'", "").replace("\n", "").strip().split(",")
            if y == int(x[-1]):
                temp.write(str(line))
                break
    temp.close()

    # printing the sorted values for the user
    details = open("sort_desc.txt", "r")
    contents = details.read()
    print(contents)
    details.close()
