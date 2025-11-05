def checkDigit(n):
    try:
        float(n)
        return True
    except Exception:
        return False

while True:
    h = input("Enter your height(m): ")
    if checkDigit(h):
        break
    else:
        print("Enter a valid number of height(m).")
    
while True:
    m = input("Enter your weight(kg): ")
    if checkDigit(m):
        break
    else:
        print("Enter a valid number of weight(kg).")

BMI = float(m) / float(h) ** 2
if BMI < 15:
    print("Laghari shadid va khatarnak.")
elif BMI >= 15 and BMI < 16:
    print("Laghari shadid.")
elif BMI >= 16 and BMI < 18.5:
    print("Laghar.")
elif BMI >= 18.5 and BMI < 25:
    print("Normal.")
elif BMI >= 25 and BMI < 30:
    print("Ezafe vazn.")
elif BMI >= 30 and BMI < 35:
    print("Chagh.")
elif BMI >= 35 and BMI < 40:
    print("Chaghi shadid.")
else:
    print("Chaghi shadid va khatarnak.")
