budget = int(input())
value = 0

while budget >= value:
    price = input()

    if price == "End":
        print("You bought everything needed.")
        break

    price = int(price)
    value += price

if budget < value:
    print(f"You went in overdraft!")
    
