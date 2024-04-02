import random

def computer_response():
    game_list = ['rock', 'paper', 'scissors']

    game_choice = random.choice(game_list)

    return game_choice


def winner(userInput, computer_output):
    if (userInput == computer_output):
        return 'It`s a tie'
    elif (userInput == 'rock' and computer_output == 'scissor') or (userInput == 'paper' and computer_output == 'rock') or (userInput == 'scissors' and computer_output == 'paper'):
        return 'You win'
    else:
        return 'computer wins'
    
def gaming (rounds):
    user_score = 0
    computer_score = 0

    for rounds in range(1, rounds + 1):
        print(f'Round {rounds}: ')
        userInput = input('Enter your choice: ')
        computer_output = computer_response() 

        print(f'Computer`s choice: {computer_output}')
        print(winner(userInput, computer_output))

        if winner(userInput, computer_output) == 'You win':
            user_score += 1
        elif winner(userInput, computer_output):
            computer_score +=1

        print(f'Score - You: {userInput}, Computer: {computer_score}\n')

        if user_score >= rounds // 2 + 1 or computer_score >= rounds // 2 + 1:
            break

    if user_score > computer_score:
        print('Congratulations! You win the game')
    elif user_score < computer_score:
        print('Sorry, the computer wins the game')
    else:
        print('It`s a tie')

gaming(2)
    


