def digitCheck(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

while True:
    number = input("Please enter your number: ")
    if digitCheck(number):
        number = float(number)
        break
    else:
        print("ERROR!! Enter a valid number.")

while True:
    r = input("Please enter base: ")
    if r.isdigit() and 1 < int(r) < 37:
        r = int(r)
        break
    else:
        print("ERROR!! Enter a valid base (2-36).")

def decimalBase(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    n1 = int(n)
    n2 = n - n1

    result1 = ""
    if n1 == 0:
        result1 = "0"
    else:
        while n1 > 0:
            remainder = n1 % base
            result1 = digits[remainder] + result1
            n1 //= base

    result2 = ""
    count = 0
    while n2 > 0 and count < 6:
        n2 *= base
        digit = int(n2)
        result2 += digits[digit]
        n2 -= digit
        count += 1
        
    return (f"{result1}.{result2}")

in_base = decimalBase(number, r)
print(f"{number} in base {r} is: {in_base}")
