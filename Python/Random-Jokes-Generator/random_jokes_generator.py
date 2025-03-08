"""
A program that stores a list of jokes and randomly selects one to display every time the user runs it. Add a fun twist with jokes about Python or programming!

DISCLAIMER!!  : The Jokes are AI-Generated
"""



import random       # to randomly select any joke from the list

jokes = [
    "Why do Python programmers prefer dark mode? Because the light attracts bugs!",
    "Why did the programmer quit his job? He didn't get arrays.",
    "Why don't programmers like nature? It has too many bugs.",
    "How do you comfort a JavaScript bug? You console it.",
    "What's a programmer's favorite hangout place? The Foo Bar.",
    "Why did the computer go to therapy? It had too many issues.",
    "What's the object-oriented way to become wealthy? Inheritance.",
    "Why do Java developers wear glasses? Because they don't see sharp.",
    "Why couldn't the Python function stop talking? It had too many arguments.",
    "Why did the HTML tag go to therapy? It felt unclosed.",
    "Why did the CSS designer break up with the HTML developer? They had style issues.",
    "Why do Python programmers love tea? Because they love to \"brew\" the perfect code.",
    "What's a programmer's favorite type of music? Algo-rhythm.",
    "What did the code say to the programmer? “You complete me!”",
    "Why was the JavaScript developer so good at sports? Because they knew how to handle events!",
    "Why did the developer go broke? Because they used all their cache.",
    "Why did the coder cross the road? To get to the other IDE.",
    "How do you make a programmer's coffee? Make sure it's Java, not JavaScript!",
    "Why don't programmers like to play hide and seek? Because good luck hiding when the debugger is looking for you.",
    "How does a programmer fix a broken chair? They debug it.",
    "What did the computer do when it saw an error? It caught the exception."
    ]


def get_random_joke():
    """
    This function picks a random joke and displays it to the user
    """
    return random.choice(jokes)

def main():
    """
    Main function - runs the random jokes generator
    """
    print("Welcome to the Random Jokes Generator App")
    input("Press Enter to hear a joke ... ")
    print("\n" + get_random_joke() + "\n")

if __name__ == "__main__":
    """
    This block ensures main() only runs when this file is directly executed.
    If someone imports this file (like a library), this block will NOT run.
    """
    main()
