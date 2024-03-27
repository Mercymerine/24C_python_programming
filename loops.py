'''
for number in range(0, 10):
    if (number % 2 == 0):
        print(f'{number} is EVEN')
    else:
        print(f'{number} is ODD')

# write a programme that prints multiples of three in a given range specified by a user
number = int(input('Enter number :'))

for number in range(0, 100):
    if (number % 3 == 0):
        print(f'{number} is divisible by 3')
    else:
        print('It is not divisible')
'''
#while loop
userInput = int(input('Enter number :'))

while (userInput < 10):
    userInput = userInput + 1
    print('I`m too young')
else:
    print('I`m here')