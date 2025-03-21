print("Your marks should be within 0 to 100")
while True:
    # Ask stuent for his/her marks
    try:
        marks_input = int(input("Enter your marks: "))

        # Check if marks are in a valid range
        if marks_input >= 0 and marks_input <= 100:
            # Grading
            if marks_input >= 90:
                print("A")
            elif marks_input >= 80:
                print("B")
            elif marks_input >= 70:
                print("C")
            elif marks_input >= 60:
                print("D")
            else:
                print("F")

            break
        else:
            print("Marks MUST be between 0 and 100")

    except ValueError:
        print("Ivalid input! Enter a number value please (0 - 100)")
