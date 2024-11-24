 # Defining a dictionary with month numbers and their corresponding days
month_days = {
    1: 31,  # January
    2: 28,  # February (non-leap year)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

# Asking the user to input the month number
month_number = int(input("Enter the month number (1-12): "))

# Checking if the input is valid
if month_number in month_days:
    if month_number == 2:  # February
        # Asking if the year is a leap year
        is_leap_year = input("Is it a leap year? (yes/no): ").strip().lower()
        days_in_february = 29 if is_leap_year == 'yes' else 28
        print(f"The number of days in month {month_number} is: {days_in_february}")
    else:
        print(f"The number of days in month {month_number} is: {month_days[month_number]}")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")