# reminder App
import calendar
import time


def taske():
    taske_name = input("What would you like to do today: ")
    taske_time = input("On What time would you like to do it: ")
    taske_date = calendar.month = int(input("What date would you like to do it: "))
    # calendar
    taskeList = [taske_date, taske_time, taske_name]

    print(f"taske\n {taske_name} , do on {taske_time}, {taske_date}")


taske()
