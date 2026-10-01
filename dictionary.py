dictionary = {
    "Water": "Water",
    "Soda": "Soda",
    "Juice": "Juice"
}
items = []
drink = input("Choose item to drink (Water, Soda, Juice): ")
print(f"You have added {dictionary[drink]} to the cart.")
keep_shopping = input("Would you like to keep shopping(Yes/No)?: ")

if keep_shopping == "Yes":
    item = input("Would you like to purchase Water, Soda, or Juice?: ")
    if item == "Water":
        print("Water has been added to the cart.")
    elif item == "Soda":
        print("Soda has been added to the cart.")
    elif item == "Juice":
        print("Juice has been added to the cart.")
    print(keep_shopping)
if keep_shopping == "No":
    print("Total: [items]")



