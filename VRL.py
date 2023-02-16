# https://stackoverflow.com/questions/73889704/python-sorting-date-without-using-build-in-function


def for_vrl():
    # adding the dates from the text file to a list
    dates = []
    with open("date_location.txt", "r") as file:
        detail = file.readlines()
        for x in detail:
            x = x.replace("[", "").replace("]", "").replace("\"", "").replace("\'", "").strip().split(" , ")

            dates.append(x[0])

    # soring the date in ascending order
    date_asc = []
    while dates:
        early_date = dates[0]
        for x in dates:
            if x < early_date:
                early_date = x

        date_asc.append(early_date)
        dates.remove(early_date)

    # printing the sorted dates

    print(date_asc)
    print("The dates are sorted in ascending order")
