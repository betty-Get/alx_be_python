# from datetime import datetime, timedelta


# def display_current_datetime():
#     global current_date
#     current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     # current_date.strftime("%X")
#     print(f"Current date and time: {current_date}")


# def calculate_future_date():
#     date_to_add = int(input(
#         "Enter the number of days to add to the current date: "))
#     future_date = int(current_date) + timedelta(days=date_to_add)
#     print(f"Future date: {future_date}")


# display_current_datetime()
# calculate_future_date()

from datetime import datetime, timedelta


def display_current_datetime():
    global current_date
    current_date = datetime.now()  # Store as datetime object
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")


def calculate_future_date():
    date_to_add = int(
        input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=date_to_add)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")


display_current_datetime()
calculate_future_date()
