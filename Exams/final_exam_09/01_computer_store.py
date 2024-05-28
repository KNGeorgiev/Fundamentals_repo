price_without_taxes = 0
total_price = 0
tax = 0

while True:

    input_value = input()
    if input_value == "special" or input_value == "regular":
        if input_value == "special":
            total_price = total_price - total_price * 0.10
        else:
            discount = 0
        break

    else:
        input_value = float(input_value)

        if input_value < 0:
            print("Invalid price!")
        else:
            price_without_taxes += input_value
            total_price += input_value + input_value * 0.20
            tax += input_value * 0.20

if total_price == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {price_without_taxes:.2f}$\n"
          f"Taxes: {tax:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_price:.2f}$\n")
