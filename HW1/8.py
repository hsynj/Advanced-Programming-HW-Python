while True:
    number = input("Please enter your number: ")
    if number.isdigit():
        number = int(number)
        break
    else:
        print("ERROR!! Enter a valid number.")
while True:
    r = input("Please enter base: ")
    if r.isdigit():
        if 0 < int(r) < 37:
            r = int(r)
            break
        else:
            print("ERROR!! Enter a valid base(1,36).")
    else:
        print("ERROR!! Enter a valid base.")


def decimalBase(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while n > 0:
        remainder = n % base
        result = digits[remainder] + result
        n //= base

    return result


def totalBase(n):
    result = 0
    while n > 0:
        remainder = n % 10
        result += remainder
        n //= 10
    return result


inBase = int(decimalBase(number, r))
print(f"{number} in base {r} is: {inBase}")

totalInBase = int(totalBase(inBase))
# print(f"{totalInBase}")

totalInBaseInBase = int(decimalBase(totalInBase, r))
print(f"Final resual is : {totalInBaseInBase}")
