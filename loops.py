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
'''
#while loop
userInput = int(input('Enter number :'))

while (userInput < 10):
    #userInput = userInput + 1
    print('I`m too young')
else:
    print('I`m here')
'''
'''
# dicitionary
    
emptyDict ={}

person ={
    'name' : 'Jack',
    'age' : 30, 
    'location' : 'Nairobi',
    'hobbies':['Basketball', 'Cycling', 'Reading']

}
print(person['hobbies'])
'''
 
# rewrite the grade analyzer challenge. You're going to represent students in a dicitoanry with their names score as key in in the dicitoanry.
'''
students = {
    'ken':[82, 12],
    'ken': [82, 12]
}
students = [
    {
        'name':'ken',
        'score': 40
    },
    {
        'name':'ken',
        'score': 56
    }
]
'''
#Finding the average for each student

student_grades = {
    'Tessie': [89, 76, 89, 65],
    'Kabete': [12, 45, 86, 34],
    'Solomom': [34, 67, 28, 10],
    'John': [11, 98, 56, 77],
    'Benjamin': [90, 34, 74, 67]
}
student_average = {}
for key, values in student_grades.items():
    student_average[key] = sum(values) / len(values)
print(student_average)

#Student with the highest average grade
highest_student = max(student_average, key=student_average.get)
#print(highest_student)
highest_grade = student_average[highest_student]
#print(highest_grade)
print(f'{highest_student} : {highest_grade}')

#Students above the threshold
pass_mark = 50
for k, v in student_average.items():
    if v > pass_mark:
        print(f'{k}: {v}')
   