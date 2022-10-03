import random

from art import logo, vs
from game_data import data

current_score = 0
game_state = True
while game_state == True:
    choiceA = random.choice(data)
    choiceB = random.choice(data)
    if choiceA == choiceB:
        choiceB = random.choice(data)
    print(logo)
    print(f"Your current score is {current_score}")
    print(f"Compare A: {choiceA['name']}, a {choiceA['description']} from {choiceA['country']}.")
    print(vs)
    print(f"Against B: {choiceB['name']}, a {choiceB['description']} from {choiceB['country']}.")
    
    def user_choice ():
        """formats user input for later comparison"""
        choice = input("Who has more followers? Select 'A' or 'B':\n")
        if choice == 'A':
            return choiceA
        if choice == 'B':
            return choiceB
    
    choice = user_choice()
    
    def count_check(input1,input2):
        '''comparison of follower count, returns highest amount'''
        if input1['follower_count'] > input2['follower_count']:
            return input1
        else:
            return input2
    
    def check_choice(a,b):
        '''checks to see if user matches reality'''
        if a == b:
            print("yay")
            return True
        else:
            print("Boo")
            return False
    
    if check_choice(choice,count_check(choiceA,choiceB)):
        current_score += 1
    else:
        game_state = False
        
print(f"your final score was {current_score}")
