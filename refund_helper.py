days_ago = int(input("How many days ago have you purchased the item?" ))
item_use = input("Have you used the item at all? y:n ")
item_broken = input("Has the item broken down on its own? y:n ")

if days_ago <= 10 and item_use == "n" or item_broken == "y":
    print("You can get a refund")
else: 
    print("You cannot get a refund")