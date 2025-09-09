import calendar

def show_calendar():
    print("📅 Calendar App")
    print("====================")
    
    # Ask user for year and month
    year = int(input("Enter year (e.g. 2025): "))
    month = int(input("Enter month (1-12): "))
    
    # Display the calendar
    print("\nHere is your calendar:\n")
    print(calendar.month(year, month))

# Run the program
if __name__ == "__main__":
    show_calendar()
