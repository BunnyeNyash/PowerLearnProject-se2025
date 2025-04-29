# Create a file and write atleast 5 lines
with open("input.txt", "w") as file:
    file.write("Hello, my name is Winter.\n")
    file.write("I am 20 years old, and will be turning 21 this coming May. I am really excited.\n")
    file.write("I am a college student, in her third year of college.\n")
    file.write("I have got three siblings, one brother and two sisters.\n")
    file.write("I love coding. Coding feels like life to me. It helps me make use of my creative mind.\n")
    file.write("I love cooking and love cooking shows to the moon and back.\n")
    file.write("My favorite go to activity is anything related to art, craft, and music, or anything to do with gun ranges and racing circuits.\n")
    
# Reads the content that we just wrote to the file
with open("input.txt", "r") as file:
    content = file.read()

    # number of words
    words = content.split()
    word_count = len(words)

    # uppercase
    uppercase = content.upper()
# processed text and word count to new file
with open("output.txt", "w") as file1:
    file1.write(f"{uppercase}\n\nThe number of words in this file is: {word_count}")

# Success message
print("Hooray!! File created successfully")
