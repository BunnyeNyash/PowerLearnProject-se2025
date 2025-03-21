# Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
list_of_integers = []
count = 0

while len(list_of_integers) < 5:
    while True:
        try:
            integer = int(input("Enter a number: "))
            list_of_integers.append(integer)
            count += integer                                     # Sum all integers in the list
            break                                                # Stop the loop
        except ValueError:
            print("Please enter a value that is a number")

print(f"The sum of all integers in the list is: {count} \n\n\n")





# Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
favorite_books = ("To Kill a Mockingbird", "Beloved", "Mrs Dalloway", "Pride and Pejudice", "Outlander")

for book in favorite_books:
    print(book)

print("\n\n\n")





# Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.

# dictionary with keys and placeholders for the values to be collected from the user
person_info = {"name" : "", "age" : 0, "favorite_color" : ""}

# Ask for user input
while True:
    name = input("Enter your name: ").title().strip()
    # print(name)


    while True:
        try:
            age = int(input(("Enter your age:  ")))
            # print(age)
            break           # stop loop after collecting the age value in numerical terms
        except ValueError:
            print("Please enter a value that is a number\n")


    favorite_color = input("Enter your favorite color: ").strip().title()
    # print(favorite_color)

    # Update the dictionary with user input
    person_info["name"] = name
    person_info["age"] = age
    person_info["favorite_color"] = favorite_color
    
    break                    # stop loop after collecting user input and updating the dictionary


print(f"\n\n{person_info}\n\n\n")





# Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.

# Placeholder for the set values from the user
set1_integer = set()
set2_integer = set()

# Ask for user input
print("Entering values for the FIRST set")
while len(set1_integer) < 5:
    while True:
        try:
            value = int(input("Enter your value: "))
            set1_integer.add(value)
            break                                       # stop the loop after values of 1st set
        except ValueError:
            print("Please enter a value that is a number")


print("\n\nEntering values for the SECOND set")
while len(set2_integer) < 5:
    while True:
        try:
            value = int(input("Enter your value: "))
            set2_integer.add(value)
            break                                       # stop the loop after values of 2nd set
        except ValueError:
            print("Please enter a value that is a number")

# new set with elements common to the two sets
new_set = set1_integer.intersection(set2_integer)


# results
print(f"\n\nFirst Set: {set1_integer}")
print(f"Second Set: {set2_integer}")
print(f"Common Elements: {new_set}\n\n\n")





# Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.


list_of_words = []              # Placeholder for the list of words from the user

# Ask for user input
while len(list_of_words) < 5:
    while True:
        word_input = input("Enter a word of your choice: ").strip()

        # test for letter words
        if word_input.isalpha():
            list_of_words.append(word_input)
            break                               # stop the loop after getting our input
        else:
            print("Invalid input. Please enter a valid word (Letters only)")

# print(list_of_words)

# Check for words with an odd number of characters
odd_character_list = [word for word in list_of_words if len(word) % 2 != 0]
print(f"\nCreated List: {list_of_words}")
print(f"Words with an odd number of characters: {odd_character_list}\n")

