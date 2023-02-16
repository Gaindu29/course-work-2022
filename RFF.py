def for_rff():
    # displaying contents of stf_file

    # printing current contents of stf_file
    rff = open("stf_file.txt", "r")
    contents = rff.read()
    print(contents)
    rff.close()

    # calling ADD function if needed
    user_in = input("you want to add more details ? (yes/no) : ")
    if user_in == "yes":
        import FUNCTIONS.ADD
        FUNCTIONS.ADD.for_add()

    # copying the data back into stf file from driver details
    with open("driver_details.txt", "r") as file:
        # changes happen to driver details, it should be copied to stf file
        with open("stf_file.txt", "w") as file2:
            for value in file:
                file2.write(str(value))

    # calling DDD function if needed
    user_in = input("you want to delete details ? (yes/no) : ")
    if user_in == "yes":
        import FUNCTIONS.DDD
        FUNCTIONS.DDD.for_ddd()

    # copying the data back into stf file from driver details
    with open("driver_details.txt", "r") as file:
        # changes happen to driver details, it should be copied to stf file
        with open("stf_file.txt", "w") as file2:
            for value in file:
                file2.write(str(value))

    # calling UDD function if needed
    user_in = input("Do you want to update details ? (yes/no) : ")
    if user_in == "yes":
        import FUNCTIONS.UDD
        FUNCTIONS.UDD.for_udd()

    # copying the data back into stf file from driver details
    with open("driver_details.txt", "r") as file:
        # changes happen to driver details, it should be copied to stf file
        with open("stf_file.txt", "w") as file2:
            for value in file:
                file2.write(str(value))

