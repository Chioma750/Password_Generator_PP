import string
import random

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
bag = ""

length = int(input("How long should your password be? "))

want_letters = input("Include letters? (yes or no) ")
want_digits = input("Include digits? (yes or no) ")
want_symbols = input("Include symbols? (yes or no) ")

if want_letters.lower() == "yes":
    bag = bag + letters
if want_digits.lower() == "yes":
    bag = bag + digits
if want_symbols.lower() == "yes":
    bag = bag + symbols

if length < 8:
    print()
    print("This password is too short to be safe")
elif bag == "":
    print()
    print("Say yes or choose any from letters, digits, or symbols")
else:
    password = ""
    print()

    for i in range(length):
        character = random.choice(bag)
        password = password + character
    print(password)
