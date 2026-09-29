import string
lenght = int(input("How long should your password be? "))
print(lenght)

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
bag = letters + digits + symbols
print(bag)