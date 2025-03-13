# Write a Python function that prompts the user to enter a number. Then, given that number, it prints the sentence "Hello, Python!" that many times.

def repeat_sentence():
    # get input from the user
    repeat_times = int(input("Enter the number of times you want a sentence repeated: "))

    repeat = 0

    while True:
        if repeat >= repeat_times:
            break
        else:
            print("Hello, Python!")
            repeat += 1


repeat_sentence()
