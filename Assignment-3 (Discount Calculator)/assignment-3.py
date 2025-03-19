# Initialize the function to calculate the discount amount and the final price after applying the discount
def calculate_discount(price, discount_percent):

    # Checking if the discount percentage is greater than or equal to 20
    if discount_percent >= 20:
        # Calculating the discount amount and the final price after applying the discount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount

        # Printing the discount amount and the final price after applying the discount
        print("The discount amount is: ", int(discount_amount))
        print("The final price after applying the discount is: ", int(final_price))
    else:
        # If the discount percentage is less than 20, no discount is applied
        print("No discount applied. The original price is: ", int(price))

# Taking input from the user for the original price and the discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calling the function to calculate the discount amount and the final price after applying the discount
calculate_discount(price, discount_percent)