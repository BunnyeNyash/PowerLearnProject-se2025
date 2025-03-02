# Check if the temperature is greater than 22 degrees.
# If true, it's a hot day. If false, it's a cool day.

# get the temperature from the user and convert it to a float
temperature = float(input("Enter the temperature in degrees Celsius: "))

if temperature > 20:
    print("What a hot day!")
else:
    print("The day is a cool one")
