'''
print(20<10)
print(20>10)
print(20<=10)
print(20>=10)
print(20==10)
'''
# if statement
if (5>4) :
    print('Hi, five')

# Python code checking for age checking whether they can vote or not
age = int(input('Enter your age'))
if (age > 18):
    print('You can vote')
else:
    print('You cannot vote')

# Extended ifs
amount = float(input('Enter withdrawal amount:'))

if (amount > 1000):
    print('You can withdraw')
elif (amount > 12000):
    print('You need to report')
elif (amount < 0):
    print('Your broke')
elif (amount > 0 and amount <= 1000):
    print('Too little to withdraw')
else:
    print('Welcome to the bank')

 # Python programme that takes in student population in a school and determines whether the school shoul get funding or not using extended if statements
    
population = int(input('Enter school population:'))

if (population < 50):
    print('You do not require school funding')
elif (population > 50 and population < 100):
    print("We will fund half of the school population")
elif (population > 100 and population < 150):
    print('We will fund you')
else:
    print('We will fund you but you will need to look for other sources to also support you')

mark=int(input('Enter yor mark '))
if(mark<40):
    print('FAIL')
elif(mark>=40 and mark<49):
    print('D')
elif(mark>=50 and mark<59):
    print('C')
elif(mark>=60 and mark<69):
    print('B')
else:
    print('A')