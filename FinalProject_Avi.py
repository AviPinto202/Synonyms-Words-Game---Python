import random

# יוצר קובץ ניקוד

f = open("score.txt", "a", encoding='utf-8')

# תפריט ראשי
def PrintMenu():
    print(15 * "-", "Welcome to Synonyms Words Game", 15 * "-")
    print(24 * "-", "MENU", 25 * "-")
    print(6 * "-", "Choose One of 4 choices (write the number)", 6 * "-")
    print("1. Start Game")
    print("2. Player Stats")  # שולח אותך לדף של התוצאות
    print("3. Explanation of the game")  # הסבר על המשחק מתלבט אם להוריד או לא
    print("0. Exit")

    print(67 * "-")


def MainMenu():
    loop = True
    # כל עוד לופ שווה true התפריט ירוץ
    # ברגע שבוחרים 0 זה יצא מהתוכנית
    while loop:
        PrintMenu()  # מציג את ההדפסות של התפריט
        choice = input("Enter your choice [0-3] \n")

        if choice == "3":
            print("In a synonym words game you need to and guess the synonym word by the list.\n"
                  "The user's answer is made by writing a word in lower case only.\n"
                  "The game over when you get 5 points or that you are wrong 5 times.\n"
                  "You can get Help , Write help in the game. But !! it will cost you in 1 point.\n"
                  "Good Luck and Enjoy!!!")
            print(67 * "-")

        elif choice == "2":  # כאן לשלוח לדף ניקוד
            print("The Score: ")
            file = open("score.txt", "r", encoding='utf-8')
            for line in file:
                print(line)

        elif choice == "1":
            print("----- The Game ( 0 to Exit) -----")
            TheGame()

        elif choice == "0":
            loop = False
            print("The program has closed")
        else:
            print("I don't understand your choice.")


def TheGame():
    # הגדרת משתנים
    # המפתח זאת המילה הראשונה ואז צריך לנחש את המילה הנרדפת שלה
    # המילה הראשונה בליטס היא המילה הנכונה שאר המילים הן רק בשביל החלק של העזרה במשחק
    words = {
        "repair": ["fix", "right", "take care"],
        "mother": ["mom", "dad", "sister"],
        "victory": ["win", "capture", "lose"],
        "blend": ["mix", "drink", "catch"],
        "purchase": ["buy", "sell", "choose"],
        "ability": ["skill", "upgrade", "strong"],
        "afraid": ["scared", "dark", "alarm"],
        "insane": ["crazy", "stupid", "hero"],
        "father": ["dad", "mom", "brother"],
        "beautiful": ["pretty", "hermosa", "nice"]
    }

    # משתנה שמכיל את שם השחקן
    player_Name = input("Enter Your Name: ")

    # הופך את המילות מפתח לליסט
    keyWord_list = list(words.keys())

    # מסדר מחדש את כל מילות המפתח כך שבכל משחק המילים יסדרו מחדש
    random.shuffle(keyWord_list)

    correct = 0  # נקודות נכונות
    incorrect = 0  # נקודות של תשובות לא נכונות

    for keyword in keyWord_list:
        print(keyWord_list)
        # print(words[keyword][0])
        # word_choose = input("-- Choose the word you want to guess --\n")
        synonyms_choose = input("-- Write the synonym in lower case only --\n")
        if synonyms_choose == "help":
            print(words.values())
        if synonyms_choose == (words[keyword][0]):
            print("Correct Answer !!")
            correct += 1
            print(correct)
            if correct >= 5:
                print("You Win !!")
                f.write("\n")
                f.write(player_Name)
                f.write("\nThe Total Correct Answer Is: ")
                f.write(str(correct))
                break
        if synonyms_choose != (words[keyword][0]):
            print("Incorrect,Try Again..")
            incorrect += 1
            print(incorrect)
            if incorrect >= 5:
                print("You Lose !!")
                f.write(player_Name)
                f.write("\nThe Total Incorrect Score Is: ")
                f.write(str(incorrect))
                break
    f.close()


MainMenu()
# TheGame()
