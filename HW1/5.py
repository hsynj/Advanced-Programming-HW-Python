def checkDigit(n):
    if n.isdigit():
        return True
    else:
        return False


def kabise(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


print("Enter like this: 06/10/1960 (day, month, year)")
# Year
while True:
    year = input("Enter the year: ")
    if checkDigit(year) and (1 <= int(year) <= 2025):
        break
    else:
        print("ERROR!! Enter a valid year.")
# Month
while True:
    month = input("Enter the month: ")
    if checkDigit(month) and 1 <= int(month) <= 12:
        break
    else:
        print("ERROR!! Enter a valid month.")
# Day
while True:
    day = input("Enter the day: ")
    if checkDigit(day):
        if 1 <= int(month) <= 6:
            if 1 <= int(day) <= 31:
                break
            else:
                print("ERROR!! Enter a valid day(1,31).")
        elif 7 <= int(month) <= 11:
            if 1 <= int(day) <= 30:
                break
            else:
                print("ERROR!! Enter a valid day(1,30).")
        else:
            if kabise((int(year))):
                if 1 <= int(day) <= 30:
                    break
                else:
                    print("ERROR!! Enter a valid day(1,30).")
            else:
                if 1 <= int(day) <= 29:
                    break
                else:
                    print("ERROR!! Enter a valid day(1,29).")
    else:
        print("ERROR!! Enter a valid day.")

magic = int(day) * int(month)

if magic == (int(year)%100):
    print("Magic Date!!")
else:
    print("Not a Magic Date!!")
