# ...............prompting the user to make a selection and getting an input.............


print("""*** WELCOME TO WORLD RALLY CROSS CHAMPIONSHIP ***

Please make a selection.


Type ADD for adding driver details
Type DDD for deleting
Type UDD for updating driver details
Type VCT for viewing the rally cross standings table
Type SRR for simulating a random race
Type VRL for viewing race table sorted according to the date
Type STF to save the current data to a text file
Type RFF to load data from the saved text file
Type ESC to exit the program""")
selection = str(input("\n Your selection is : "))  # getting the option user wants

# converts to uppercase if entered in lowercase
selection = selection.upper()

# ==================================  MAIN PROGRAM  ===============================


# -----------text file----------------
details = open("driver_details.txt", "a+")
data = open("stf_file.txt", "a+")


# ..............importing the functions according to the user input..........


if selection == "ADD":
    import FUNCTIONS.ADD
    FUNCTIONS.ADD.for_add()


elif selection == "DDD":
    import FUNCTIONS.DDD
    FUNCTIONS.DDD.for_ddd()


elif selection == "UDD":
    import FUNCTIONS.UDD
    FUNCTIONS.UDD.for_udd()


elif selection == "VCT":
    import FUNCTIONS.VCT
    FUNCTIONS.VCT.for_vct()


elif selection == "SRR":
    import FUNCTIONS.SRR
    FUNCTIONS.SRR.for_srr()


elif selection == "VRL":
    import FUNCTIONS.VRL
    FUNCTIONS.VRL.for_vrl()


elif selection == "STF":
    import FUNCTIONS.STF
    FUNCTIONS.STF.for_stf()


elif selection == "RFF":
    import FUNCTIONS.RFF
    FUNCTIONS.RFF.for_rff()


elif selection == "ESC":
    exit()

else:
    print("Invalid Input")