import time

while True:

    print("Hello welcome to the online quiz 1.0!")

    print("Can I have your name please?")

    name = input()

    print("Hello", name, "how are you today?")

    mood = input()

    if mood == "good":

        print("Good for you.")



    elif mood == "bad":

        print("Im sorry to hear that.")



    else:

        print("Okay.")

    print("Are you ready?")

    ready = input()

    time.sleep(1)

    if ready == "yes":

        print("Okay", name, "here it is:")

        time.sleep(1)

        number = 3

        while number > 0:
            print(number)

            time.sleep(1)

            number = number - 1

        score = 0

        print("Question 1.")

        time.sleep(2)

        print("Entertainment")

        time.sleep(0.5)

        print("In what christmas movie did Dwayne Johnson play in?")

        time.sleep(1)

        print("  a. Jumanji  /  b. Red One  /  c. Red Notice")

        ans1 = input("Answer here:  ")

        if ans1 == "b":

            score = score + 1

            time.sleep(1)

            print("Thats correct!")

            print("Your score is:", score, "points!")



        elif ans1 == "a":

            score = score - 1

            print("Close guess. Try agian")

            ans2 = input("Anser, second try:  ")

            if ans2 == "b":

                print("You answered it correct on your second try")

                score = score + 1

                time.sleep(1)

                print("Your score is", score, "points!")



            elif ans2 == "c":

                score = score - 1

                print("Thats wrong. Try again on the next question!")

                time.sleep(1)

                print("Your score is", score, "points!")



        elif ans1 == "c":

            score = score - 1

            print("Close guess. Try agian!")

            ans2 = input("Anser, second try:  ")

            if ans2 == "b":

                print("You answered it correct on your second try!")

                score = score + 1

                time.sleep(1)

                print("Your score is", score, "points!")



            elif ans2 == "a":

                score = score - 1

                print("Thats wrong. Try again on the next question!")

                time.sleep(1)

                print("Your score is", score, "points!")



        else:

            print("This answer is not excepted in this quiz!")

        time.sleep(1)

        print("Are you ready for the next question?")

        nextt = input()

        if nextt == "yes":

            print("Okay", name, "here it is!")

            time.sleep(1)

            number = 3

            while number > 0:
                print(number)

                time.sleep(1)

                number = number - 1

            time.sleep(1)

            print("Trivia!")

            time.sleep(0.5)

            print("Is the Netherlands a monarchy?")

            print("a. yes. /  b. no")

            ans3 = input("Answer here:   ")

            if ans3 == "a":

                time.sleep(1)

                print("That is absoloutly correct!")

                score = score + 1

                print(name, "you have", score, "points!")



            elif ans3 == "b":

                time.sleep(1)

                print("Close, but wrong!")

                score = score - 1

                time.sleep(1)

                print(name, "you have", score, "points!")







            else:

                print("This answer is not excepted!")

            time.sleep(1)

            print("Are you ready?")

            again55 = input()

            if again55 == "yes":

                print("Okay!")

                number = 3

                while number > 0:
                    print(number)

                    time.sleep(1)

                    number = number - 1

                print("Question 3 ...")

                time.sleep(1)

                print("Entertainment:")

                time.sleep(1)

                print("Who played in the movie ''Mission Imposible''?")

                time.sleep(1)

                print(" a. Tom Cruise  /  b. Dwayne Johnson  /  c. Jack Black")

                ans4 = input("Answer here:  ")

                if ans4 == "a":

                    score = score + 1

                    time.sleep(1)

                    print("Thats correct!")

                    print("Your score is:", score, "points!")



                elif ans4 == "b":

                    score = score - 1

                    print("Close guess. Try agian")

                    ans5 = input("Anser, second try:  ")

                    if ans5 == "a":

                        print("You answered it correct on your second try")

                        score = score + 1

                        time.sleep(1)

                        print("Your score is", score, "points!")



                    elif ans5 == "c":

                        score = score - 1

                        print("Thats wrong. Try again on the next question!")

                        time.sleep(1)

                        print("Your score is", score, "points!")



                elif ans4 == "c":

                    score = score - 1

                    print("Close guess. Try agian!")

                    ans5 = input("Anser, second try:  ")

                    if ans5 == "a":

                        print("You answered it correct on your second try!")

                        score = score + 1

                        time.sleep(1)

                        print("Your score is", score, "points!")



                    elif ans5 == "b":

                        score = score - 1

                        print("Thats wrong. Try again on the next question!")

                        time.sleep(1)

                        print("Your score is", score, "points!")



                else:

                    print("This answer is not excepted in this quiz!")

                time.sleep(1)

                print("You have made it 3 questions into the quiz!")

                time.sleep(1)

                print("Are you ready for the second last question?")

                again567 = input()

                if again567 == "yes":

                    print("Okay...")

                    number = 3

                    while number > 0:
                        print(number)

                        time.sleep(1)

                        number = number - 1

                    time.sleep(1)

                    print("Geography!")

                    time.sleep(1)

                    print("In what continent is the sahara desert located?")

                    time.sleep(1)

                    print("a. Europe  /  b. Africa  /  c. Australia")

                    ans6 = input("Answer here:  ")

                    if ans6 == "b":

                        score = score + 1

                        time.sleep(1)

                        print("Thats correct!")

                        print("Your score is:", score, "points!")



                    elif ans6 == "a":

                        score = score - 1

                        print("Close guess. Try agian")

                        ans7 = input("Anser, second try:  ")

                        if ans7 == "b":

                            print("You answered it correct on your second try")

                            score = score + 1

                            time.sleep(1)

                            print("Your score is", score, "points!")



                        elif ans7 == "c":

                            score = score - 1

                            print("Thats wrong. Try again on the next question!")

                            time.sleep(1)

                            print("Your score is", score, "points!")



                    elif ans6 == "c":

                        score = score - 1

                        print("Close guess. Try agian!")

                        ans2 = input("Anser, second try:  ")

                        if ans7 == "b":

                            print("You answered it correct on your second try!")

                            score = score + 1

                            time.sleep(1)

                            print("Your score is", score, "points!")



                        elif ans7 == "a":

                            score = score - 1

                            print("Thats wrong. Try again on the next question!")

                            time.sleep(1)

                            print("Your score is", score, "points!")



                    else:

                        print("This answer is not excepted in this quiz!")

                    time.sleep(1)

                    print("Moving on...")

                    number = 3

                    while number > 0:
                        print(number)

                        time.sleep(1)

                        number = number - 1

                    time.sleep(1)

                    print("History:")

                    time.sleep(1)

                    print("Which ancient civilasation built the pyramids?")

                    time.sleep(1)

                    print("a. Ancient Egypt  /  b. Ancient Rome  /  c. Ancient Greece")

                    ans8 = input("Answer here:  ")

                    if ans8 == "a":

                        score = score + 1

                        time.sleep(1)

                        print("Thats correct!")

                        print("Your score is:", score, "points!")



                    elif ans8 == "b":

                        score = score - 1

                        print("Close guess. Try agian")

                        ans9 = input("Anser, second try:  ")

                        if ans9 == "a":

                            print("You answered it correct on your second try")

                            score = score + 1

                            time.sleep(1)

                            print("Your score is", score, "points!")



                        elif ans9 == "c":

                            score = score - 1

                            print("Thats wrong. Try again on the next question!")

                            time.sleep(1)

                            print("Your score is", score, "points!")



                    elif ans8 == "c":

                        score = score - 1

                        print("Close guess. Try agian!")

                        ans9 = input("Anser, second try:  ")

                        if ans9 == "a":

                            print("You answered it correct on your second try!")

                            score = score + 1

                            time.sleep(1)

                            print("Your score is", score, "points!")



                        elif ans9 == "b":

                            score = score - 1

                            print("Thats wrong. Try again on the next question!")

                            time.sleep(1)

                            print("Your score is", score, "points!")



                    else:

                        print("This answer is not excepted in this quiz!")

                    print("Congrats on finishing!")

                    time.sleep(1)

                    print("You earned", score, "points in total!")

                    print("Do you want to play again?")

                    playagain = input()

                    if playagain == "yes":

                        time.sleep(5)



                    else:

                        print("Thank you for playing!")

                        break



                else:

                    print("Goodbye", name, "see you!")

                    time.sleep(1)

                    print("You earned", score, "points in total!")

                    print("Do you want to play again?")

                    playagain = input()

                    if playagain == "yes":

                        time.sleep(5)



                    else:

                        print("Please give us a rating!")

                        break



            else:

                print("Goodbye", name, "see you!")

                time.sleep(1)

                print("You earned", score, "points in total!")

                print("Do you want to play again?")

                playagain = input()

                if playagain == "yes":

                    time.sleep(5)



                else:

                    print("Please give us a rating!")

                    break



        else:

            print("Goodbye", name, "see you!")

            time.sleep(1)

            print("You earned", score, "points in total!")

            print("Do you want to play again?")

            playagain = input()

            if playagain == "yes":

                time.sleep(5)



            else:

                print("Please give us a rating!")

                break



    else:

        print("Goodbye", name, "see you!")

        time.sleep(1)

        print("You earned 0 points in total!")

        print("Do you want to play again?")

        playagain = input()

        if playagain == "yes":

            time.sleep(5)



        else:

            print("Please give us a rating!")

            break

time.sleep(5)

print("Give this quiz a honest rating out of 10!")

rating = input()

print("Thank you for your rating (", rating, ")!")

time.sleep(1)

print("This will be forwarded to the creator.")

time.sleep(1)

print("Thank you for playing!")

time.sleep(3)

print()

print()

import random

heleluja = random.randint(1, 10)

if heleluja == (7):

    print("You got lucky and got a free trial of quiz 2.0!")

    print("Would you like to play quiz 2.0 online for free?")

    quiz12 = input()

    if quiz12 == "yes":

        print("Starting in...")

        number = 3

        while number > 0:
            print(number)

            time.sleep(1)

            number = number - 1

        score2 = 0

        print("Question 1...")

        time.sleep(1)

        print("Trivia!")

        time.sleep(1)

        print("What is the biggest state in Germany?")

        print("a. Hessen  /  b. Brandenburg  /  c. Bavaria")

        ans21 = input("Answer here:  ")

        if ans21 == "c":

            time.sleep(1)

            print("Thats correct!")

            score2 = score2 + 1

            print("You have", score2, "points in total!")



        elif ans21 == "b":

            time.sleep(1)

            print("Thats wrong try again!")

            score2 = score2 - 1

            time.sleep(1)

            ans212 = input("Try again:   ")

            time.sleep(1)

            if ans212 == "c":

                time.sleep(1)

                print("You got it correct on your second try!")

                score2 = score2 + 1

                print("You have", score2, "points now", name, "!")



            elif ans212 == "a":

                print("You got it wrong on both tries!")

                time.sleep(1)

                print("Better luck on the next question!")



        elif ans21 == "a":

            score2 = score2 - 1

            print("Close guess. Try agian")

            ans212 = input("Anser, second try:  ")

            if ans212 == "c":

                print("You answered it correct on your second try")

                score2 = score2 + 1

                time.sleep(1)

                print("Your score is", score2, "points!")



            elif ans212 == "b":

                score2 = score2 - 1

                print("Thats wrong. Try again on the next question!")

                time.sleep(1)

                print("Your score is", score2, "points!")



        else:

            print("This answer is not excepted!")

        time.sleep(1)

        print("Are you enjoying this quiz so far?")

        feedback = input()

        if feedback == "good":

            print("Thank you for your opinion!")

            time.sleep(1)

            print("This will be forwarded to the creator!")



        else:

            time.sleep("1")

            print("I hope we can make it up in the next quiz!")

        print("Last test question!")

        time.sleep(1)

        number2 = 3

        while number2 > 0:
            print(number2)

            time.sleep(1)

            number2 = number2 - 1

        time.sleep(1)

        print("Question 2. ")

        time.sleep(1)

        print("Geography!")

        print("In what city does the Eifel Tower stand?")

        print("a. Paris  /  b  Berlin  /  c. London:")

        ans22 = input("Answer here:  ")

        if ans22 == "a":

            score2 = score2 + 1

            time.sleep(1)

            print("Thats correct!")

            print("Your score is:", score2, "points!")



        elif ans22 == "b":

            score2 = score2 - 1

            print("Close guess. Try agian")

            ans221 = input("Anser, second try:  ")

            if ans221 == "a":

                print("You answered it correct on your second try")

                score = score + 1

                time.sleep(1)

                print("Your score is", score2, "points!")



            elif ans221 == "c":

                score2 = score2 - 1

                print("Thats wrong. Try again on the next question!")

                time.sleep(1)

                print("Your score is", score2, "points!")



        elif ans22 == "c":

            score2 = score2 - 1

            print("Close guess. Try agian!")

            ans221 = input("Anser, second try:  ")

            if ans221 == "a":

                print("You answered it correct on your second try!")

                score2 = score2 + 1

                time.sleep(1)

                print("Your score is", score2, "points!")



            elif ans221 == "b":

                score2 = score2 - 1

                print("Thats wrong. Try again on the next question!")

                time.sleep(1)

                print("Your score is", score2, "points!")



        else:

            print("This answer is not excepted in this quiz!")



    else:

        print("Okay!")

    time.sleep(1)

    print("This quiz is only available once!")

    time.sleep(1)

    print("I hpe you enjoyed this test quiz!")

    time.sleep(1)

    print("If you use the code ''first quiz'' you can play the complete second quiz online!")





