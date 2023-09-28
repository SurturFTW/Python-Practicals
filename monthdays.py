import calendar
month = int(input("Enter month: "))
year = int(input("Enter year: "))
num_days = calendar.monthrange(year, month)[1]
print("Number of days is", num_days)
