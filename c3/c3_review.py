import random

# Review: Strings and Conditional Statements

# 1. Creating Strings
greeting = "Hello, World!"
name = 'Alice'

# 2. Printing Strings
print(greeting)
print(name)

# 3. Concatenation
full_greeting = greeting + " " + name
print(full_greeting)
print(greeting, name)


# 4. String Length
length = len(full_greeting)  # 19
print("The length of the full greeting is: " + str(length))
print(f"The length of the full greeting is: {length}")
print("The length of the full greeting is: {length}")


# 5. Indexing
first_char = name[0]
print(f"The first character in the name is: {first_char}")
names = ["adrian", "joey", "tom", "ethan", "jack", "gemma",
         "pete", "hintash", "maryam", "veronica", "amy", "todd"]  # 12 개
idx = int(random.random() * len(names))
print(f"The name at index {idx + 1} is {names[idx]}")
print(idx)


# 6. Slicing
first_four_names = names[:4]
print(f"The first four names in the list are: {first_four_names}")
names234 = names[2:5]
print(names234)

# 7. Negative Indexing
last_char = name[-1]
print(f"The last character in the name is: {last_char}")

# 8. Changing Case
print(name.upper())
print(name.lower())

# 9. Finding a Substring
gibberish = "adfhjhsbfjb wjehfjdh puqer jlfkvh aoibfj lawenfihpajsdbf jasndfioew"
want = "dhpu"
n = gibberish.find(want)
print(n)

# 10. Replacing a Substring
new_greeting = full_greeting.replace("World", "Everyone")
print(new_greeting)

# 11. Splitting a String
words = full_greeting.split()
print(words)

# 12. Conditional Statements
# Simple if statement
age = 18
if age >= 18:
    print("You are an adult.")

# If/else statement
temperature = 25
if temperature > 30:
    print("It's a hot day.")
else:
    print("It's a cool day.")

# If/elif/else statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Comparison operators
x = 10
y = 20
print(x == y)  # False
print(x != y)  # True
print(x < y)   # True
print(x > y)   # False
print(x <= y)  # True
print(x >= y)  # False


# Data Type / Structure
# string, int, float, boolean
# list, dictionary, tuple, ...
# we can make new data structures
