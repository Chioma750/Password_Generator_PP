import string
import random

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
bag = letters + digits + symbols

length = int(input("How long should your password be? "))

password = ""

for i in range(length):
    character = random.choice(bag)
    password = password + character
print(password)