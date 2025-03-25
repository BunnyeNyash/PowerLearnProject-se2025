def calculate_discount(price=100, discount_percent=30):
    """
    Determines the final price after applying a discount.

    Parameters:
    price (float): The original price of the item.
    discount_percent (int): The discount percentage.

    Returns:
    float: The final price after applying the discount, or the original price if the discount is less than 20%.
    """
    # apply discount if greater than 20%, else charge the original price
    if discount_percent >= 20:
        discount = discount_percent / 100
        final_price = price - (price * discount)
        return final_price
    else:
        return price


def main():
    """
    Handles user input and calls the discount calculation function.
    Ensures valid numerical input before calling calculate_discount.
    """
    while True:
        # catch errors
        try:
            # ask for user input (price & discount_percentage)
            price = float(input("Enter the original price: "))
            discount_percent = int(input("Enter your discount percentage: "))

            # call the function with the user input
            final_price = calculate_discount(price, discount_percent)   # store the return value
            print(f"The final price is: {final_price:.2f}")
            break         # break from the loop after getting a valid input
        
        except ValueError:
            print("Invalid input. Please enter a valid numerical value")


if __name__ == "__main__":
    main()
