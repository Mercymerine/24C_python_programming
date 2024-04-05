import random

def get_computer_choice():
    choices  = ['rock', 'paper', 'scissors']
    return random.choice(choices)

#get_computer_choice()

def winner(user_choice, computer_choice):
    if (user_choice == computer_choice):
        return 'It`s a tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors'):
        return 'You win'
    elif (user_choice == 'rock' and computer_choice == 'paper'):
        return 'You win'
    elif (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'You win'
    else:
        return 'Computer wins!'
    
def play_game(num_rounds):
    user_score = 0
    computer_score = 0

    for round_num in range(1, num_rounds + 1):
        print(f'Round {round_num}')
        user_choice = input('Enter your choice: ')
        computer_choice = get_computer_choice()

        print(f'Computer`s choice: {computer_choice}')
        print(winner(user_choice, computer_choice))

        if (winner(user_choice, computer_choice) == 'You win'):
            user_score += 1
        elif (winner(user_choice, computer_choice) == 'Computer wins'):
            computer_score += 1

        print(f'Score - You: {user_score}, Computer: {computer_score}\n')

        if (user_score >= num_rounds // 2 + 1 or computer_score >= num_rounds // 2 + 1):
            break

        if (user_score > computer_score):
            print('Congratulations! You win the game!')
        elif (user_score < computer_score):
            print('Sorry computer wins the game')
        else:
            print('It`s a tie!')

if __name__ == '__main__':
    num_rounds = int(input('How many rounds do you want to play? '))
    play_game(num_rounds)

    