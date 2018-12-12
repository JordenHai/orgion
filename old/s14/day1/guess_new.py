# -*- coding:utf-8 -*-
# Author: Jorden Hai

age_of_oldboy = 56
def func(guess_age):
    if guess_age == age_of_oldboy :
         return 1
    elif guess_age > age_of_oldboy:
         return 2
    elif guess_age < age_of_oldboy:
         return 3
    else:
         print("wrong input")
         return -1

print('Let us guess the age!')

def input_age():
    try:
        age = int(input("input the guess age:"))
        return age
    except ValueError:
        print("ValueError!")

guess_age = input_age()
count = 0
while count < 3:
    count = count + 1
    temp = func(guess_age)
    if temp == 1:
        print("yes,you got it.")
        break
    elif temp == 2:
        print("The age you guess is bigger ")
        guess_age = input_age()
        continue
    elif temp == 3:
        print("The age you guess is Smaller ")
        guess_age = input_age()
        continue
    elif temp == -1:
        break



