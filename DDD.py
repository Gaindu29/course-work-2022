# used to delete a driver
def for_ddd():
    # getting name to remove
    name_remove = input("\nEnter the name of the driver to be removed : ")

    # opening the driver file to read the details
    with open("driver_details.txt", "r") as fileR:
        # opening a temp file to write the driver details one by one
        with open("tempfile.txt", "w") as fileW:
            x = fileR.readlines()
            # For 1 drivers
            for i in x:
                value = i.replace("[", "").replace("]", "").replace("\"", "").replace("\'", "").replace("\n", "").\
                    split(", ")

                # if the driver name is not equal to the driver list[0] it will write the line into temp file
                if name_remove != value[0]:
                    fileW.write(str(i))


        fileW.close()
    fileR.close()

    # save the content in temp file to the driver file(basically it will duplicate the data)
    with open("tempfile.txt", "r") as file:
        with open("driver_details.txt", "w") as file2:
            for value in file:
                file2.write(str(value))

     # to display the file content after deletion
    details = open("driver_details.txt", "r")
    contents = details.read()
    print(contents)
    details.close()