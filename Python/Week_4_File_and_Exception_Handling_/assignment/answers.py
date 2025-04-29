# Instructions:
print("Here is a list of possible file extensions for the file that you are going to add: ")

print("1)  .txt\n2)  .csv\n3)  .log\n4)  .json\n5)  .xml\n6)  .md\n7)  .py")
print("8)  .html\n9)  .htm\n10) .ini\n11) .yaml\n12) .yml\n13) .rtf\n\n\n")

while True:
    # ask user for file
    filename = input("Please enter the name of your file: ")

    # Open the user's file and read it
    try:
        with open(filename, "r") as file:
            content = file.read()

            # count the words
            words = content.split()
            word_count = len(words)

            # uppercase
            uppercase = content.upper()
        

        # write output to a new file
        with open("upper.txt", "w") as file_output:
            file_output.write(uppercase)
            file_output.write(f"\n\nThe total number of words in this file is: {word_count}")
        
        
        # reverse the file
        with open(filename, "r") as file:
            content1 = file.readlines()   # reads the lines into a list
            reversed_lines = content1[ : : -1]  # reverse the list


        # write output to a new file
        with open("reversed.txt", "w") as file_reversed:
            file_reversed.write("".join(reversed_lines))

        print("Hooray! The files have been created successfully")

        break


    except FileNotFoundError:
        print("ERROR: The file CAN NOT be found or DOESN'T exist.")

    except IOError:
        print("ERROR: There was a problem reading the file.")

