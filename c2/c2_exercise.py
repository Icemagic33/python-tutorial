# Password Strength Checker
password = input("Enter a password: ")

if len(password) < 6:
    print("Password is too short.")
elif not any(char in "!@#$%^&*()_+" for char in password):
    print("Password should contain at least one special character.")
else:
    print("Password is strong.")

# Simple Chatbot
user_input = input("You: ")  # user_input = "how are YOU doing"
# user_input.lower()  # "how are you doing"
if "hello" in user_input.lower():  # False
    print("Chatbot: Hi there!")
elif "how are you" in user_input.lower():  # True
    print("Chatbot: I'm just a bot, but I'm doing great!")
else:
    print("Chatbot: I don't understand.")

# Palindrome Checker
user_input = input("Enter a string: ")
if user_input == user_input[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# Age Calculator
birth_year = int(input("Enter your birth year: "))
current_year = 2024
age = current_year - birth_year

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")


'''
24.06.10 Homework:
1. Create a program that takes a string input from the user and prints whether it is a palindrome or not.
2. Write a program that asks the user for their birth year and calculates their age. Print a message based on the age (e.g., "You are a teenager," "You are an adult," etc.).
'''
