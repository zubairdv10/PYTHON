#Zubair De vries , Class 2
#Python Lottery Project

current_year = 2020
year_of_birth = int(input('Enter Year Of Birth: '))
age = current_year - year_of_birth
mytext = 'You are %s years old.'
print(mytext % age)
if age < 18:
    print('You are underage and cannot participate')
    exit()
else:
    print('You are allowed to enter the Lotto competition')

import random
#List for lottery numbers
lotteryNumbers = []

for i in range (0,6):
    number = random.randint(1,49)
    while number in lotteryNumbers:
        number = random.randint(1,49)

    lotteryNumbers.append(number)
#List in ascending
lotteryNumbers.sort()

participantsNumbers = []
for i in range(0,6):
    number = int(input("Please enter your number between 1 and 49: "))
    while number<1 or number>49:
        number= int(input("Try again:Please enter your number between 1 and 49: "))
    participantsNumbers.append(number)

participantsNumbers.sort()

print("The lottery numbers are:")
print(lotteryNumbers)

print("Lotto numbers that you have selected:")
print(participantsNumbers)

counter=0
for number in participantsNumbers:
    if number in lotteryNumbers:
        counter +=1

print("You have " + str(counter) + " number(s) ")

if counter <=1:
    print("I'm sorry but you do not have enough correct numbers to win any money ")
elif counter ==2:
    print("Congratulations you have just won yourself R20.00")
elif counter ==3:
    print("Congratulations you have just won yourself R100.50")
elif counter ==4:
    print("Congratulations you have just won yourself R2384.00")
elif counter ==5:
    print("Congratulations you have just won yourself R8584.00")
elif counter ==6:
    print("Congratulations you have just won yourself the biggest prize of all R10 000 000 .00")

from datetime import date
today = date.today()
print("Today's date:", today)



with open ("Results of lottery.txt", "w") as output:
    output.write(str("The Winning Numbers are:")+ '\n')

    output.write(str(lotteryNumbers)+ '\n')

    output.write(str("Your numbers are:"+ '\n'))

    output.write(str(participantsNumbers)+ '\n')

    output.write(str("Amount of correct numbers")+ '\n')

    output.write(str(counter)+ '\n')

    output.write(str("Date the lottery was played:")+ '\n')

    output.write(str(today) + '\n')

    output.write(str("The participant who has 1 or 0 correct numbers wins no money") + '\n')

    output.write(str("The participant who has 2 correct numbers wins R20.00") + '\n')

    output.write(str("The participant who has 3 correct numbers wins R100.50") + '\n')

    output.write(str("The participant who has 4 correct numbers wins R2384.00") + '\n')

    output.write(str("The participant who has 5 correct numbers wins R8584.00") + '\n')

    output.write(str("The participant who has all correct numbers wins R10 000 000.00") + '\n')

print("Date lottery was played:", today)

import doctest
doctest.testfile("Results of Lottery.txt")