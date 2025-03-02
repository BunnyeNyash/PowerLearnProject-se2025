# Write a while loop that keeps asking the user to enter a number.
# The loop should stop only when the user enters 0.


while True:
    number = int(input("Enter a whole number: "))       # Ask the user for a number
    
    if number == 0:
        print("Done!")
        break
