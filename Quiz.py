print("Welcome to 'The TEN' type 'yes' when ready")
import random 
#WE DO WORK HERE 
#EEASY
Questions = ["\n---What's two plus two??--- ", "\n---Who lives in a pineapple under the sea??--- ", "\n---Wich is better Python or Java??--- ", "\n---I am justice I am the night who am I??--- ", "\n---How many days do we have in a week?--- ", "\n---How many cents are in a quarter?--- ", "\n---Which sport does Kyrie Irving play?--- ", "\n---How many “Wonders of the World” are there?--- ", "\n---Is a square a perallelogram?--- ", "\n---In Sesame Street, who lives in the trash can?--- "]
Answers = ["4", "Spongbob", "Python", "Batman", "7", "25", "Basketball", "7", "Yes", "Oscar The Grouch"]

#MEDIUM
Questions_M = ["\n---how many ounces in a gallon--- ", "\n---How many states of the United States?--- ", "\n---How many legs spiders have?--- ", "\n---Which is the largest and deepest ocean in the world?--- ", "\n---The periodic table has how many elements?--- ", "\n---Who was the ancient Roman goddess of love?--- ", "\n---What famous ship sank in 1912?--- ", "\n---Who carved Pinocchio in Disney’s Pinocchio?--- "]
Answers_M = ["128", "50", "8", "Pacific Ocean", "118", "Venus", "Titanic", "Geppetto"]

#HARD
L = 3
points = 0
Difficulty = 0
Questions_H =["\n---Solve for X: 8x + 16 = 24--- ", "\n---What was the first state to ratify the Constitution?--- ", "\n---What elements can be found in the first column of the periodic table?--- ", "\n---What type of triangle has two sides equal in length?--- ", "\n---Which scientist is credited with the laws of motion?--- ", "\n---What is the capital of Spain?--- ", "\n---What’s the name of Donald Duck’s sister?--- "]
Answers_H = ["1", "Delaware","Alkali Metals", "Isosceles", "Newton", "Madrid", "Della"]


#IMPOSSIBLE

Questions_I = ["\n---What gets wetter the more it dries?--- ", "\n---What word is spelled incorrectly in every single dictionary?--- ", "\n---What can be broken but never held?--- ", "\n---What is it that lives if it is fed, and dies if you give it a drink?--- ", "\n---Everyone in the world needs it, but they usually give it without taking it. What is it?--- "]
Answers_I = ["Towel", "Incorrectly", "Promise", "Fire", 'Advice']

#WORK ABOVE 
playing = input("Want to play? ")
if playing != "yes":
    print("Thats to bad, see you later then")
    quit()



#GAME BELIRE 

print("""\nOkay here's how it works you'll be given a set of questions if you get them right you get a point get ten points and you win...
But here's the catch get one wrong and you lose a life don't worry tho you have three watch-out questions do get harder 
after each question press enter to continue 
---If you need to be refreshed on the rules type 'Help' on any wuestion and the rules will show 
That's enough talking let's begin
---Press enter to start--- """)
ready = input(" ")

#Questions first two easy
while (points < 10 and Difficulty <= 2):
    R = random.randint(0,9)

    answer = input(Questions[R])
    if answer == Answers[R]:
        points +=1
        Difficulty += 1
        print("\nPoints: ", points, "\nLives:  ", L, "\nCorrect- Great job you gained a point")
        ready = input(" ")

    elif answer == "Help":
        print("""\nNeed help playing don't worry here are the rules
        ---Rules--
        1. Reach 10 points and win the game
        2. lose all three lives and you lose :(
        ---Specifics---
        1. for numbered answers questions please type the number 
        2. For word-answered questions please capitalize the beginning of each word

        Press enter when ready to join the game again 
        """)
        ready = input(" ")
        

    elif L == 0:
            print("\nPoints: ", points, "\nLives:  ", L, "\nWrong- Ouch! so close but yet so far thank you for playing try again if you dare...")
            quit()

    elif points == 0:
            L -= 1
            print("\nPoints: ", points, "\nLives:  ", L, "\nWrong- Thats not quite right try another")
            ready = input(" ")

    else:
        if points > 0:
            L -= 1
            points -= 1 
            print("\nPoints: ", points, "\nLives:  ", L, "\nWrong- come on you can do better than that")
            ready = input(" ")




#PART TWO
print("\n----Good job so far I think its time to turn up the heat----")
while (points < 10 and Difficulty >= 3 and Difficulty < 6):
    
    R = random.randint(0,7)

    answer = input(Questions_M[R])
    if answer == Answers_M[R]:
        points +=1
        Difficulty += 1
        print("\nPoints: ", points, "\nLives:  ", L, "\nCorrect- Great job you gained a point")
        ready = input(" ")

    elif answer == "Help":
        print("""\nNeed help playing don't worry here are the rules
        ---Rules--
        1. Reach 10 points and win the game
        2. lose all three lives and you lose :(
        ---Specifics---
        1. for numbered answeres questions please type the number 
        2. For word-answered questions please capitalize the begining of each word

        Press enter when ready to join the game again 
        """)
        ready = input(" ")
        

    elif L == 0:
            print("\nPoints: ", points, "\nLives:  ", L, "\nWrong- Ouch! so close but yet so far thank you for playing try again if you dare...")
            quit()

    elif points == 0:
            L -= 1
            print("\nPoints: ", points, "\nLives:  ", L, "\nWrong- Thats not quite right try another")
            ready = input(" ")

    else:
        if points > 0:
            L -= 1
            points -= 1 
            print("\nPoints: ", points, "\nLives:  ", L, "\nWrong- come on you can do better than that")
            ready = input(" ")




#PART THREE HARD 
#FEET
#TOES

print("\n----So you think you're smart huh?? Well try this----")
while (points < 10 and Difficulty >= 6 and Difficulty <= 8):
    R = random.randint(0,6)

    answer = input(Questions_H[R])
    if answer == Answers_H[R]:
        points +=1
        Difficulty += 1
        print("\nPoints: ", points, "\nLives:  ", L, "\nCorrect- Great job you gained a point")
        ready = input(" ")

    elif answer == "Help":
        print("""\nNeed help playing don't worry here are the rules
        ---Rules--
        1. Reach 10 points and win the game
        2. lose all three lives and you lose :( 
        ---Specifics---
        1. for numbered answeres questions please type the number 
        2. For word-answered questions please capitalize the begining of each word

        Press enter when ready to join the game again 
        """)
        ready = input(" ")
        

    elif L == 0:
            print("\nPoints: ", points, "\nLives:  ", L, "\nWrong- Ouch! so close but yet so far thank you for playing try again if you dare...")
            quit()

    elif points == 0:
            L -= 1
            print("\nPoints: ", points, "\nLives:  ", L, "\nWrong- Thats not quite right try another")
            ready = input(" ")

    else:
        if points > 0:
            L -= 1
            points -= 1 
            print("\nPoints: ", points, "\nLives:  ", L, "\nWrong- come on you can do better than that")
            ready = input(" ")
    
print("\n----Ok, you are Pretty smart but how are you with riddles?... ready??----")
ready = input(" ")



while (points > 6 and Difficulty >= 9):
    R = random.randint(0,4)

    answer = input(Questions_I[R])
    if answer == Answers_I[R]:
        points +=1
        if points == 10:
            print("\n---Congratulations you beat The TEN but can you do it again???....---")
            quit()
        Difficulty += 1
        print("\nPoints: ", points, "\nLives:  ", L, "\nCorrect- Great job you gained a point")
        ready = input(" ")

    elif answer == "Help":
        print("""\nNeed help playing don't worry here are the rules
        ---Rules--
        1. Reach 10 points and win the game
        2. lose all three lives and you lose :(
        ---Specifics---
        1. for numbered answeres questions please type the number 
        2. For word-answered questions please capitalize the begining of each word

        Press enter when ready to join the game again 
        """)
        ready = input(" ")
        

    elif L == 0:
            print("\nPoints: ", points, "\nLives:  ", L, "\nWrong- Ouch! so close but yet so far thank you for playing try again if you dare...")
            quit()

    elif points == 10:
        #END GOAL 
        print("Congratulations you beat The TEN but can you do it again??....")
        quit()


    elif points == 0:
            L -= 1
            print("\nPoints: ", points, "\nLives:  ", L, "\nWrong- Thats not quite right try another")
            ready = input(" ")

    else:
        if points > 0:
            L -= 1
            points -= 1 
            print("\nPoints: ", points, "\nLives:  ", L, "\nWrong- come on you can do better than that")
            ready = input(" ")



#END GOAL 
