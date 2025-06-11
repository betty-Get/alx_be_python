from datetime import datetime


def display_current_datetime():
    current_date = datetime.now()
    # current_date.strftime("%X")
    print(f"Current date and time: {current_date}")


display_current_datetime()
