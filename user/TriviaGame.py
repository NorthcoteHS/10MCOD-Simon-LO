"""
Prog:Trivia Game
Name:Simon Lo
Date:08/05/2018
Desc: a quiz on a topic of my choosing
"""
#create a function linking the question to the answer
def answer():
    print('answer')
#asking a question
question = ['do birds cherp?', 'do birds sing?', 'do chocolates taste good?', 'how many music genres are out there?']
#Answer to the questions
answers = ['Yes', 'i dont know', 'Yes they taste very good', '1,264']
#to loop and pick a qusetion for the user to answer
for i, item in enumerate(question):
    print (item)
    input ('Answer:')
    print (answers[i])
