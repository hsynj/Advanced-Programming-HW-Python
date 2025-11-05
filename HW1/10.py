def checkDigit(n):
    try:
        float(n)
        return True
    except Exception:
        return False


list = []
while True:
    n = input("Enter an entry(\"-1\" for exit): ")
    if n == "-1":
        print("OK! Here is your list: ", list)
        break
    if checkDigit(n):
        if float(n) > 0:
            list.append(float(n))
        else:
            print("ERROR!! Enter an positive number.")
    else:
        print("ERROR!! Enter an invalid entry.")

ascents = []
currentAscent = 0
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        currentAscent += 1
    else:
        ascents.append(currentAscent)
        currentAscent = 0
ascents.append(currentAscent)

print(ascents)
print(f"{max(ascents)}")
