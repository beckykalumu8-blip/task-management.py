print("Welcome to Python Pizza Order Calculator!\n")

while True:
    pizza_size = input("Enter pizza size (small or large): ").lower()
    if pizza_size in ["small", "large"]:
        break
    else:
        print("Invalid pizza size. Please enter 'small' or 'large'.")

try:
    num_toppings = int(input("Enter number of additional toppings: "))
    if num_toppings < 0:
        raise ValueError("Number of toppings cannot be negative.")
except ValueError as e:
    print(f"Invalid input for toppings: {e}. Please restart and enter a non-negative integer.")
    exit()

try:
    delivery_distance = float(input("Enter delivery distance in miles: "))
    if delivery_distance < 0:
        raise ValueError("Delivery distance cannot be negative.")
except ValueError as e:
    print(f"Invalid input for distance: {e}. Please restart and enter a non-negative number.")
    exit()

if pizza_size == "small":
    base_cost = 8
elif pizza_size == "large":
    base_cost = 12

toppings_cost = num_toppings * 1 

if delivery_distance <= 5:
    delivery_fee = 2
else:
    extra_miles = delivery_distance - 5
    delivery_fee = 2 + extra_miles * 1

total_cost = base_cost + toppings_cost + delivery_fee

print("\n----- Order Summary -----")
print(f"Pizza size: {pizza_size.capitalize()}")
print(f"Number of toppings: {num_toppings}")
print(f"Delivery distance: {delivery_distance} miles")
print(f"Base cost: ${base_cost}")
print(f"Toppings cost: ${toppings_cost}")
print(f"Delivery fee: ${delivery_fee}")
print(f"Total cost: ${total_cost:.2f}")
print("--------------------------")
print("Thank you for your order!")

