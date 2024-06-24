import random

# Question 1: String Manipulation and Indexing
# Task: Create a string variable with a sentence of your choice. Print the sentence, and then:
# Print the length of the sentence.
# Extract and print the first 5 characters of the sentence.
# Replace a word in the sentence with another word of your choice and print the new sentence.
sentence = "Python programming is fun and educational."


# Question 2: Conditional Statements
# Task: Write a program that asks the user for their  score in a test. Use conditional statements to:
# Grade the user's score as follows: A (90 and above), B (80-89), C (70-79), F (below 70).
score = int(input("Enter your test score: "))


# Question 3: List and Random Indexing
# Task: Create a list of at least 5 different fruits. Use the random module to select a random fruit from the list and print it. Then:
# Convert the selected fruit's name to uppercase and print it.
# Check if the fruit's name contains the letter 'a' and print the result.
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
selected_fruits = ...

# Question 4: Iterating Over a List
# Task: You are given a list of colors. Write a program that performs the following tasks:
# 1) Iterates over the list of colors using a for loop.
# 2) Prints each color along with its position (index) in the list.
# 3) Counts and prints the total number of colors in the list.
colors = ["red", "blue", "green", "yellow", "purple",
          "orange", "pink", "brown", "black", "white"]

count = 0

for ... in ...:
    print(f"Color [color name] is at [color position]")

print(f"There are total of {count} number of colors.")

# DO NOT : use the len() function
# -> DO NOT DO THIS: count =  len(colors)
