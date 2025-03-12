import random

# the question's bank
quiz_questions = [
    {
        "question" : 'Who is the legendary designer behind the timeless "little black dress"?',
        "choices" : ["A. Christian Dior", "B. Yves Saint Laurent", "C. Coco Chanel", "D. Giorgio Armani"],
        "correct_answer" : "C",
        "fun_fact" : "Before Coco, black was for mourning. She redefined this by introducing the little black dress (LBD) in 1926, and making black a symbol of sophistication"
    },
    {
        "question" : "Which stylish First Lady in the '60s set fashion trends across the nation?",
        "choices" : ["A. Nancy Reagan", "B. Jacqueline Kennedy", "C. Michelle Obama", "D. Hillary Clinton"],
        "correct_answer" : "B",
        "fun_fact" : "Jackie Kennedy popularized pillbox hats and tailored suits, inspiring an era of 'Jackie Style' that still influences fashion today."
    },
    {
        "question" : "Which designer is credited with popularizing the wrap dress in the 1970s?",
        "choices" : ["A. Donna Karan", "B. Diane von Fürstenberg", "C. Carolina Herrera", "D. Betsey Johnson"],
        "correct_answer" : "B",
        "fun_fact" : "The wrap dress was a game-changer because it flattered all body types and was easy to wear. No zippers, just tie and go!"
    },
    {
        "question" : "Vera Wang is synonymous with which type of attire?",
        "choices" : ["A. Evening gowns", "B. Casual wear", "C. Wedding dresses", "D. Sportswear"],
        "correct_answer" : "C",
        "fun_fact" : "Vera Wang started designing wedding dresses after struggling to find her own dream dress for her wedding in 1989."
    },
    {
        "question" : "Which Italian luxury brand, founded in 1913, is known for its nylon bags and minimalist aesthetic?",
        "choices" : ["A. Fendi", "B. Gucci", "C. Prada", "D. Versace"],
        "correct_answer" : "C",
        "fun_fact" : "Prada’s iconic nylon bags became a trend in the 1990s"

    },
    {
        "question" : "Which fashion icon, born in 1973, has graced countless magazine covers?",
        "choices" : ["A. Naomi Campbell", "B. Tyra Banks", "C. Cindy Crawford", "D. Kate Moss"],
        "correct_answer" : "B",
        "fun_fact" : "Before she became a TV mogul, Tyra was rejected by multiple modeling agencies for being 'too curvy'. She proved them wrong by becoming the first Black woman on the cover of Sports Illustrated's Swimsuit Issue. Smize!"
    },
    {
        "question" : "What is the first name of the designer famously known as Chanel?",
        "choices" : ["A. Gabrielle", "B. Colette", "C. Isabelle", "D. Madeleine"],
        "correct_answer" : "A",
        "fun_fact" : "'Coco' was Gabrielle Chanel's nickname, which she adopted from a song she used to sing in her early career as a cabaret performer."
    },
    {
        "question" : "What is the nationality of the renowned fashion designer Kenzo Takada?",
        "choices" : ["A. Chinese", "B. American", "C. Japanese", "D. Thai"],
        "correct_answer" : "C",
        "fun_fact" : "Kenzo Takada was the first Japanese designer to achieve fame in the Parisian fashion industry."
    },
    {
        "question" : "Which luxury brand is known for its signature red-soled shoes?",
        "choices" : ["A. Manolo Blahnik", "B. Jimmy Choo", "C. Christian Louboutin", "D. Prada"],
        "correct_answer" : "C",
        "fun_fact" : "The red soles were inspired by a bottle of nail polish. Louboutin saw his assistant painting her nails and thought it would be perfect for shoes."
    },
    {
        "question" : "Who introduced the classic Polo clothing line?",
        "choices" : ["A. Tommy Hilfiger", "B. Calvin Klein", "C. Ralph Lauren", "D. Hugo Boss"],
        "correct_answer" : "C",
        "fun_fact" : "Ralph Lauren originally sold only neckties before expanding into the full Polo brand."

    },
    {
        "question" : 'Which high-end shoe brand was frequently featured in "Sex and the City"?',
        "choices" : ["A. Manolo Blahnik", "B. Gucci", "C. Louboutin", "D. Ferragamo"],
        "correct_answer" : "A",
        "fun_fact" : "Carrie Bradshaw’s love for Manolos turned the brand into a pop culture icon. One episode even featured her getting mugged, and all she cared about was her Manolos."
    },
    {
        "question" : "Who took over the Versace fashion house after Gianni Versace's death in 1997?",
        "choices" : ["A. Giorgio Armani", "B. Miuccia Prada", "C. Donatella Versace", "D. Domenico Dolce"],
        "correct_answer" : "C",
        "fun_fact" : "Donatella had to take over her brother's brand after his tragic murder, on 15th July, 1997."
    },
    {
        "question" : "Which French fashion designer is known for the revolutionary 'New Look' post-World War II?",
        "choices" : ["A. Hubert de Givenchy", "B. Pierre Balmain", "C. Christian Dior", "D. Jean-Paul Gaultier"],
        "correct_answer" : "C",
        "fun_fact" : "Dior's 'New Look' with cinched waists and full skirts brought back glamour after the war's fabric rationing."
    },
    {
        "question" : "Lesley Lawson is better known by what name in the fashion world?",
        "choices" : ["A. Twinggy", "B. Dovima", "C. Twiggy", "D. Veruschka"],
        "correct_answer" : "C",
        "fun_fact" : "Twiggy was the original 'it-girl' of the 1960s, famous for her big eyes, short hair, and ultra-skinny frame. She set the trend for the 'mod' look."
    },
    {
        "question" : "Which iconic French designer launched his own brand in 1961?",
        "choices" : ["A. Yves Saint Laurent", "B. Pierre Cardin", "C. André Courrèges", "D. Emanuel Ungaro"],
        "correct_answer" : "A",
        "fun_fact" : "YSL changed fashion forever by introducing the first tuxedo suit for women, called 'Le Smoking.'"
    },
    {
        "question" : "Which former Spice Girl launched her own fashion line in 2004?",
        "choices" : ["A. Mel B", "B. Geri Halliwell", "C. Victoria Beckham", "D. Emma Bunton"],
        "correct_answer" : "C",
        "fun_fact" : "Despite early skepticism, Victoria 'Posh Spice' Beckham proved she wasn't just a pop star. Her sleek, minimalist fashion brand is now a global success."
    },
    {
        "question" : "DKNY is the signature line of which designer?",
        "choices" : ["A. Donna Karan", "B. Diane von Fürstenberg", "C. Carolina Herrera", "D. Betsey Johnson"],
        "correct_answer" : "A",
        "fun_fact" : "DKNY was created for busy city women who wanted stylish yet comfortable clothes for day and night."
    },
    {
        "question" : "Which 1935 invention revolutionized women's undergarments by providing support and shape?",
        "choices" : ["A. Girdle", "B. Corset", "C. Bra", "D. Bustier"],
        "correct_answer" : "C",
        "fun_fact" : "Before the modern bra, women were stuck wearing corsets—so uncomfortable that some even caused health problems."
    },
    {
        "question" : "What accessory is commonly associated with rockstars like Axl Rose of Guns N' Roses?",
        "choices" : ["A. Fedora", "B. Bandana", "C. Leather bracelet", "D. Sunglasses"],
        "correct_answer" : "B",
        "fun_fact" : "The bandana wasn't just for style. Rockstars like Axl Rose wore them to keep sweat out of their eyes while performing."
    },
    {
        "question" : "Espadrilles are typically worn on which part of the body?",
        "choices" : ["A. Hands", "B. Head", "C. Feet", "D. Waist"],
        "correct_answer" : "C",
        "fun_fact" : "Espadrilles date back to the 14th century in Spain and were originally worn by peasants."
    },
    {
        "question" : "Carnaby Street, a fashion hub in the '60s, is located in which city?",
        "choices" : ["A. New York", "B. Paris", "C. London", "D. Milan"],
        "correct_answer" : "C",
        "fun_fact" : "Carnaby Street was the heart of the Swinging Sixties, home to icons like The Beatles and The Rolling Stones."
    },
    {
        "question" : "Cornrows are a traditional style of what?",
        "choices" : ["A. Clothing", "B. Hairstyle", "C. Footwear", "D. Jewelry"],
        "correct_answer" : "B",
        "fun_fact" : "Cornrows have been around for thousands of years, originating in Africa. They were also used as maps for escape routes during slavery."
    },
    {
        "question" : "Which bathing suit made its debut in 1946 and was considered controversial at the time?",
        "choices" : ["A. Monokini", "B. Tankini", "C. Bikini", "D. One-piece"],
        "correct_answer" : "C",
        "fun_fact" : "The bikini was so shocking when it debuted that no professional model was willing to wear it, so the designer had to hire a burlesque dancer to debut it instead."
    },
    {
        "question" : "Which Italian luxury fashion house is known for its distinctive Baroque style and black and gold designs?",
        "choices" : ["A. Versace", "B. Dolce & Gabbana", "C. Prada", "D. Valentino"],
        "correct_answer" : "A",
        "fun_fact" : "Versace's bold, flashy style is inspired by Greek mythology, hence the Medusa logo."
    },
    {
        "question" : "Which American brand, established in 1969, became a symbol of relaxed, casual fashion and is known for its denim?",
        "choices" : ["A. Levi's", "B. Gap", "C. Wrangler", "D. American Eagle"],
        "correct_answer" : "B",
        "fun_fact" : "The name 'Gap' refers to the generation gap between adults and teenagers."
    },
    {
        "question" : "Which French fashion house is famous for its perfumes, especially the iconic No. 5, introduced in 1921?",
        "choices" : ["A. Chanel", "B. Dior", "C. Givenchy", "D. Lanvin"],
        "correct_answer" : "A",
        "fun_fact" : "Chanel No. 5 was one of the first perfumes to blend multiple floral scents instead of using a single note."
    },
    {
        "question" : "Which German sportswear brand, founded in 1949, is known for its three-stripe logo?",
        "choices" : ["A. Puma", "B. Reebok", "C. Adidas", "D. Under Armour"],
        "correct_answer" : "C",
        "fun_fact" : "Adidas got its name from its founder, Adolf 'Adi' Dassler."
    },
    {
        "question" : "Which American designer is known for luxurious red carpet gowns featuring intricate beadwork and embroidery?",
        "choices" : ["A. Oscar de la Renta", "B. Michael Kors", "C. Marc Jacobs", "D. Tom Ford"],
        "correct_answer" : "A",
        "fun_fact" : "His gowns have been worn by multiple First Ladies, including Jacqueline Kennedy and Michelle Obama."
    },
    {
        "question" : "Which French fashion house, founded by Hubert de Givenchy in 1952, is known for elegant haute couture and Audrey Hepburn's iconic little black dress in 'Breakfast at Tiffany's'?",
        "choices" : ["A. Balenciaga", "B. Yves Saint Laurent", "C. Balmain", "D. Givenchy"],
        "correct_answer" : "D",
        "fun_fact" : "Givenchy and Audrey Hepburn had a lifelong friendship, and he designed many of her most famous looks."
    },
    {
        "question" : "Which British designer, known for her punk and new wave fashion, designed the famous Union Jack dress worn by Geri Halliwell of the Spice Girls?",
        "choices" : ["A. Stella McCartney", "B. Alexander McQueen", "C. Vivienne Westwood", "D. Paul Smith"],
        "correct_answer" : "C",
        "fun_fact" : "Westwood helped shape the punk fashion movement in the 1970s, making ripped clothes, safety pins, and bold prints stylish."
    }  
]


# show the user the game Rules
print("""
The quiz consists of multiple-choice questions.
Each question has four answer choices labeled A, B, C, or D.
You select your answer by typing the letters A, B, C, or D.
Each correct answer earns 1 point.
At the end of the quiz, you can see your final score.
You can choose to play again by answering the question "Do you want to play again? with a yes or a no.
      If you type "yes", the quiz restarts. If you type "no", the game exits.
""")


# ask the user for their consent to play; if "yes" play, if "no" exit the game
while True:
    proceed = input("Do you want to proceed with the game, yes or no?: ").strip().lower()

    if proceed == "yes":
        # shuffle the way the list of questions is ordered in our question's bank and then select the first 10 questions to be used in the quiz game
        random.shuffle(quiz_questions)
        selected_questions = quiz_questions[:10]

        score = 0

        # Show the question to the user and let them input ther answer
        for index, current_question in enumerate(selected_questions, 1):
            print(f'\nQuestion {index}: {current_question["question"]}')
            print("\n".join(current_question["choices"]))
            user_answer = input("Enter an answer (A, B, C, or D): ").strip().upper()

            # Checking the correctness of the user's answer and keeping a track of the same
            if user_answer == current_question["correct_answer"]:
                print(f'Correct!!  :  {current_question["fun_fact"]}')
                score += 1

            else:
                print(f'Wrong!! The correct answer was {current_question["correct_answer"]}  :  {current_question["fun_fact"]}')


        print(f"Your final score is {score}/10")
        print("Game over btw!!")


        while True:
            replay = input("\nDo you want to play again, yes or no? : ").strip().lower()
            
            if replay == "yes":
                break
            elif replay == "no":
                print("Goodbye! Till next time")
                exit()
            else:
                print("Wrong input. Only 'yes' or 'no' is allowed. Try again.")
    
    elif proceed == "no":
        print("Goodbye!")
        exit()
    else:
        print("Wrong input. Only 'yes' or 'no' is allowed. Try again.")


