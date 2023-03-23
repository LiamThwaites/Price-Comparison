'''
  Name: 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''

def compare_prices(budget, products):
    # Create a dictionary to store unit prices of each product
    prices = {}

    # Loop through each product and calculate the unit price
    for product, info in products.items():
        unit_price = info["price"] / info["quantity"]
        prices[product] = unit_price

    # Sort the products by unit price
    sorted_products = sorted(prices.items(), key=lambda x: x[1])

    # Find the best value product within the budget
    best_product = None
    for product, unit_price in sorted_products:
        if unit_price <= budget:
            best_product = product
        else:
            break

    # Print the unit prices of each product
    print("Unit prices:")
    for product, unit_price in sorted_products:
        print(f"{product}: {unit_price}")

    # Print the recommendation
    if best_product:
        print(f"Best value for money: {best_product}")
    else:
        print("Sorry, no product within budget.")

# Example usage
budget = float(input("Enter your budget: "))

products = {}

# Ask user to input information for each product
for i in range(4):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    
    # Add product to dictionary
    products[name] = {"price": price, "quantity": quantity}
  
compare_prices(budget, products)