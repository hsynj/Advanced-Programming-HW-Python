suger = 1.5 / 48
butter = 1 / 48
soda = 2.75 / 48
while True:
    n = input("Enter the count of cookies: ")
    if n.isdigit():
        break
    else:
        print("Enter a valid number.")
        continue
print("Suger: ", suger * int(n))
print("Butter: ", butter * int(n))
print("Soda: ", soda * int(n))