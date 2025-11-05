restaurants = [
    # Name, Vegetarian, Vegan, Gluten-Free
    [" Joe\'s Gourmet Burgers", 0, 0, 0],
    [" Main Street Pizza Company", 1, 0, 1],
    [" Corner Cafe", 1, 1, 1],
    [" Mama\'s Fine Italian", 1, 0, 0],
    [" The Chef\'s Kitchen", 1, 1, 1],
]

while True:
    vegetarian = input("Is anyone in your party a vegetarian? (Y/n): ")
    if vegetarian.lower() == "y":
        vegetarian = 1
        break
    elif vegetarian.lower() == "n":
        vegetarian = 0
        break
    else:
        print("Enter a valid option.(Y/n)")
        continue
while True:
    vegan = input("Is anyone in your party a vegan? (Y/n): ")
    if vegan.lower() == "y":
        vegan = 1
        break
    elif vegan.lower() == "n":
        vegan = 0
        break
    else:
        print("Enter a valid option.(Y/n)")
        continue
while True:
    gluten = input("Is anyone in your party a gluten-free? (Y/n): ")
    if gluten.lower() == "y":
        gluten = 1
        break
    elif gluten.lower() == "n":
        gluten = 0
        break
    else:
        print("Enter a valid option.(Y/n)")
        continue

validRestaurants = []
for restaurant in restaurants:
    name, isVegetarian, isVegan, isGluten = restaurant
    if (vegetarian <= isVegetarian) and (vegan <= isVegan) and (gluten <= isGluten):
        validRestaurants.append(name)

print("Here are your restaurant choices:")
if validRestaurants:
    for res in validRestaurants:
        print(f"  - {res}")
else:
    print("Sorry, no restaurants match your criteria.")
