# A program that asks for the user’s name and favorite color, then prints a personalized greeting like: “Hello, [Name]! Your favorite color, [Color], is awesome!”

def personalized_greeting(name, color):
    """
    This function returns a personalized message using the name and the color from the user
    """
    return f"Hello, {name}! Your favorite color, {color}, is awesome!"


def main():
    """
    Main function - runs all tests
    """
    name = input("Enter your name: ")
    color = input("Enter your favorite color: ")
    print(personalized_greeting(name, color))


if __name__ == "__main__":
    """
    This block ensures main() only runs when this file is directly executed.
    If someone imports this file (like a library), this block will NOT run.
    """
    main()
