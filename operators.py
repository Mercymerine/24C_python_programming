# mathematical operations in python
num1 = int(input('Enter the first number: '))

num2 = int(input('Enter the second number: '))

print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 * num2)
print(num1 % num2)

# Write a python code that calculates the sales profits for a business
'''
    Provide the expected income
    Provide the current income with profit
    Profit = current income - expected income
'''
expected_income = int(input('Enter expected income'))
current_income = int(input ('Enter current income'))
profit = (current_income - expected_income)
print(profit)