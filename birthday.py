import calendar
import os
from datetime import date
from datetime import timedelta

today = date.today()

def getBD():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            bdMonth = int(input("What month were you born in? (Type the corresponding number)\n 1 - January\n 2 - February\n 3 - March\n 4 - April\n 5 - May\n 6 - June\n"
                            " 7 - July\n 8 - August\n 9 - September\n 10 - October\n 11 - November \n 12 - December\n"))
            if bdMonth not in range(1, 13):
                raise ValueError
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:
            break
    
    inputMonth = date(today.year, bdMonth, 1)
    lastDay = calendar.mdays[inputMonth.month]
    
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            bdDay = int(input("What day were you born on?\n"))
            if bdDay not in range(1, lastDay + 1):
                raise ValueError
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:
            break
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    bd = date(today.year, bdMonth, bdDay)
    return bd

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    bd = getBD()
    
    if bd < today:
        if bd == (date.today() - timedelta(days=1)):
            print ("Your birthday already went by %d day ago." % ((today-bd).days))
        else:
            print ("Your birthday already went by %d days ago." % ((today-bd).days))

        bd = bd.replace(year=today.year + 1)
        time_to_bd = abs(bd - today)
        print (time_to_bd.days, "days until your next birthday!")
        input("\nPress the 'Enter' key to exit the program.")
        os.system('cls' if os.name == 'nt' else 'clear')
    elif bd == today:
        print("Your birthday is today! Happy Birthday!")
        input("\nPress the 'Enter' key to exit the program.")
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        time_to_bd = abs(bd - today)
        if time_to_bd.days == 1:
            print ("Your birthday is in", time_to_bd.days, "day!")
        else:
            print ("Your birthday is in", time_to_bd.days, "days!")
        input("\nPress the 'Enter' key to exit the program.")
        os.system('cls' if os.name == 'nt' else 'clear')

main();