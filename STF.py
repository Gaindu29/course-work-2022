def for_stf():
    # saving the data in driver_details to stf_file
    with open("driver_details.txt", "r") as file:
        # copying data in driver_details into stf_file
        with open("stf_file.txt", "w+") as file2:
            for value in file:
                file2.write(str(value))

            print("\nYour data has been successfully saved to stf.txt")
