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

while guess_age != 0:
    temp = func(guess_age)
    if temp == 1:
        print("yes,you got it.")
        break
    elif temp == 2:
        print("The age you guess is bigger ")
        guess_age = int(input("Guess Age:"))
        continue
    elif temp == 3:
        print("The age you guess is Smaller ")
        guess_age = int(input("Guess Age:"))
        continue
    elif temp == -1:
        break



