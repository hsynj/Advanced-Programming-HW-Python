def digitCheck(n):
    if n.isdigit():
        return True
    else:
        return False


def checkTwo(list):
    for i in range(len(list) - 1):
        if list[i] == 2:
            if list[i + 1] == 2:
                return True
            else:
                return False


def checkFour(list):
    for i in range(len(list) - 1):
        if list[i] == 4:
            if list[i + 1] == 4:
                return True
            else:
                return False

array = []
while True:
    n = input("Enter a number(\"-1\" for exit): ")
    if n == "-1":
        print("Okay, here is your list of numbers: ", array)
        break
    if digitCheck(n):
        array.append(int(n))
    else:
        print("Enter a valid number.")
        continue

if (checkTwo(array) and checkFour(array)):
    print("False")
elif (checkTwo(array) or checkFour(array)):
    print("True")
else:
    print("False")