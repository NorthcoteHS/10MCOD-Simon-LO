"""
Program: Magic 8 ball
Name: Simon Lo
Date: 21/02/18
Desc: to randomized the answer
"""

ans = 'true'
while ans:
    qusetion = ("Ask the magic 8 ball a qusetion: (press enter to quit)")
    answers = random.randint(1,8)
    if qusetion == "":
        sys.exit()
    if answer == 1:
        print ("Yes, that is a good idea")
    if anwer == 2:
        print ("No, that is a horrible choice")
    if answer == 3:
        print ("I am not sure if that is the best idea")
    if answer == 4:
        print ("This is your own decision to make, I will belive on your choice")
    if answer == 5:
        print ("You should pick a different choice")
    if answer == 6:
        print ("The choice you have chosen is the best for you")
    if answer == 7:
        print ("Chould you ask the question again")
    if answer == 8:
         print ("Don't ask me") 
