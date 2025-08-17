#1. Create a function named calculate_discount(price, discount_percent) 
# that calculates the final price after applying a discount. 
# The function should take the original price (price) 
# and the discount percentage (discount_percent) as parameters. 
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.

#2. Using the calculate_discount function, 
# prompt the user to enter the original price of an item and the discount percentage. 
# Print the final price after applying the discount, 
# or if no discount was applied, print the original price.


# Define the function
def calculate_discount(price, discount_percent):
    # Condition Statement to Calculate Discount.
    if discount_percent >= 20:
        discount = (discount_percent / 100) * price
        new_price = price - discount

        return new_price
    
    else:
        return price



# TRY..EXCEPT Error Handling In Case User Gives Wrong Input.
print("Discount is applied only if the discount price is equal or greater than 20%.\n")
try:
    original_price = float(input("Enter the price of the item (e.g: 129.21): ₦"))
    discount_price = float(input("Enter the discount percentage of the item (e.g: 12.3): "))

    final_price = calculate_discount(original_price, discount_price)

    # Condition Statement to Print Result
    if discount_price >= 20:
        print(f"\nAfter a discount of {discount_price:.3f}% was applied, New Price: ₦{final_price:.2f}.")
    
    else:
        print(f"\nAfter a discount of {discount_price:.3f}% was applied, New Price: ₦{final_price:.2f}.")

except ValueError:
    print("Invalid Input!.\nPlease enter valid numerical values for price and discount.")


# Test run the function with various number examples.
# print(calculate_discount(price= "", discount_percent= ""))

