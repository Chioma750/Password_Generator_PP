import string
import random

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
bag = letters + digits + symbols

length = int(input("How long should your password be? "))

Letters = input("yes" or "no")
Digits = input("yes" or "no")
Symbols = input("yes" or "no")

if Letters + Digits + Symbols == "yes": 

if length < 8:
    print("This password is too short to be safe")
else:
    password = ""
    print(password)

    for i in range(length):
        character = random.choice(bag)
        password = password + character
    print(password)
