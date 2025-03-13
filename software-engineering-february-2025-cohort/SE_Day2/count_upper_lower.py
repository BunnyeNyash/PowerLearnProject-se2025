# Write a Python function that takes a string as input and returns a dictionary containing the number of uppercase and lowercase characters in the string. Any characters that cannot be categorized as uppercase or lowercase (e.g., symbols) should be counted as "other".

def count_uppercase_lowercase_other():
    # Get string from user
    string_1 = input("Enter your string: ")

    # dictionary for storing the values for uppercase, lowercase, and other characters
    char_count = {
        "uppercase" : 0,
        "lowercase" : 0,
        "other" : 0
    }

    string_list = list(string_1)

    for char in string_list:
        if char.isupper():
            dict["uppercase"] += 1
        elif char.islower():
            dict["lowercase"] += 1
        else:
            dict["other"] += 1

    return dict

# invoke the function
print(count_uppercase_lowercase_other())
