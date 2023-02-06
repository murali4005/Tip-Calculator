# Tip Calculator

print('Welcome to the Tip Calculator.\n')

bill = float(input('What was the total bill? $'))
num_of_people = int(input('How many people to split the bill? '))
percentage = float(input('What Percentage tip would you like to give? 10, 12, or 15? '))

bill_for_each_person = round((bill + (bill * percentage / 100)) / num_of_people,2)

print(f'Each person should pay: ${bill_for_each_person}')