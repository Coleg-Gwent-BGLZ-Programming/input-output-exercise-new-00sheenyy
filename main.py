print("Welcome to the Smoothie Shop!")

# Ask the user for their name using input()
name = input("What is your name? ")

# Ask how many smoothies they want to buy
smoothie_count = input(f"Hi {name}! How many smoothies would you like to buy? ")

# Convert the number of smoothies to an integer
smoothie_count = int(smoothie_count)

# Calculate the total cost (each smoothie costs £3.50)
cost_per_smoothie = 3.50
total_cost = smoothie_count * cost_per_smoothie

# Ask if the customer wants a reusable cup for £1.00 extra
reusable_cup = input("Would you like a reusable cup for an extra £1.00? (yes/no) ").lower()

# If the customer wants a reusable cup, add the cost
if reusable_cup == "yes":
    total_cost += 1.00

# Display the final total cost
print(f"Thanks for your order, {name}! Your total for {smoothie_count} smoothies is £{total_cost:.2f}.")

