import random

def get_computer_choice():
    word_list = ['psyche', 'quiz', 'cobweb', 'matrix', 'lengths', 'larynx','mnemonic', 'lucky']
    computer_response = random.choice(word_list)
    #print(computer_response)
    for word in computer_response:
        return'-'
        

#get_computer_choice()
        
def get_user_choice():
    userInput = input('Enter your choice  of letters for each word: ')
    for  letter in userInput:
        return letter

#get_user_choice()
    
def comparison(rounds):
    user = 0
    computer = 0

    for round in r
    


