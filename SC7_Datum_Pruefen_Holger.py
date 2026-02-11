# DIFFICULTY: 3
# TASK: Schreibe ein Programm, welches ein Datum auf Korrektheit prüft.
#       Dazu soll eine Variable "date_valid" auf 1 gesetzt werden, wenn
#       das Datum valide ist.
#       Teste mit verschiedenen, sowohl korrekten als auch falschen Daten.
#
# Beispiele:
# 29.02.1999 - date_valid: 0
# 29.02.2000 - date_valid: 1
# 13.05.2000 - date_valid: 1
# 32.05.2000 - date_valid: 0
# 24.13.2000 - date_valid: 0
# 
# CHALLENGE: Berücksichtige auch die speziellen Schaltjahresregeln (nicht durch 100
#            aber durch 400 teilbar).

day, month, year = 29, 2, 2020
long_months = [1, 3, 5, 7, 8, 10, 12]


def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def is_month(month):
    return 1 <= month <= 12


def is_day(day):
    return 1 <= day <= 31


def print_day(day):
    if day < 10:
        return "0" + str(day)
    else:
        return str(day)


def print_month(month):
    if month < 10:
        return "0" + str(month)
    else:
        return str(month)


def date_valid(day, month, year):
    is_leap_year(year)
    is_month(month)
    is_day(day)
    if is_leap_year(year) and is_month(month) and month == 2 and day <= 29:
        day = print_day(day)
        month = print_month(month)
        print(f"{day}.{month}.{year} is a valid date.")
    elif not is_leap_year(year) and is_month(month) and month == 2 and day <= 28:
        day = print_day(day)
        month = print_month(month)
        print(f"{day}.{month}.{year} is a valid date.")
    elif is_month(month) and month != 2 and month in long_months and is_day(day) and day <= 31:
        day = print_day(day)
        month = print_month(month)
        print(f"{day}.{month}.{year} is a valid date.")
    elif is_month(month) and month != 2 and month not in long_months and is_day(day) and day <= 30:
        day = print_day(day)
        month = print_month(month)
        print(f"{day}.{month}.{year} is a valid date.")
    else:
        day = print_day(day)
        month = print_month(month)
        print(f"{day}.{month}.{year} is no valid date.")
        
        
date_valid(29, 2, 1999)
date_valid(29, 2, 2000)
date_valid(13, 5, 2000)
date_valid(32, 5, 2000)
date_valid(24, 13, 2000)
date_valid(13, 5, 2023)
date_valid(29, 2, 2024)
date_valid(30, 2, 2025)
date_valid(1, 3, 2011)
date_valid(29, 2, 2222)