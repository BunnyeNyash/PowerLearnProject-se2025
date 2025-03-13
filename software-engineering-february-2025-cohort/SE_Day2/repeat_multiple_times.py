# Write a Python function that prompts the user to enter a number and their name. Then, given that number, it prints the sentence "Hello, {name}" that many times.


def repeat_multiple_times():
    # ask for the user's input
    name = input("Enter your name: ").title()
    repeat_times = int(input("Enter the number of times you want to see hello: "))

    for _ in range(repeat_times):
        print(f"Hello {name}")

# invoke the function
repeat_multiple_times()
