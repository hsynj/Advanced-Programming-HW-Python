while True:
    p = input("Enter the amount of principal originally deposited into the account: ")
    if p.isdigit():
        break
    else:
        print("ERROR!! Enter a valid number of principal.")

while True:
    intrestPaid = input("Enter the annual interest rate paid by the account(1-100%): ")
    if intrestPaid.isdigit():
        if int(intrestPaid) > 0 and int(intrestPaid) < 101:
            break
        else:
            print("ERROR!! Enter a valid interest rate(1,100).")
    else:
        print("ERROR!! Enter a valid interest rate.")

r = float(intrestPaid) / 100

while True:
    n = input("Enter the number of times per year that the interest is compounded(if monthly:12 , if quarterly: 4) ")
    if n.isdigit() and int(n) > 0:
        break
    else:
        print("ERROR!! Enter a valid number of times.")

while True:
    t = input("Enter the number of years the account will be left to earn interest: ")
    if t.isdigit() and int(t) > 0:
        break
    else:
        print("ERROR!! Enter a valid number of years.")

a = float(p) * (1 + (float(r) / float(n))) ** (float(n) * float(t))
print(f"The amount of money that will be in the account after the specified number of years is: {a:.2f}")