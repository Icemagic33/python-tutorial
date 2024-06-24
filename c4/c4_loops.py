# Lecture 3: Loops and Iteration

# 1. Introduction to Loops
print("Loops allow you to iterate over a sequence of values.")

# 2. For Loops
print("\nFor Loops:")

# Simple for loop
print("Simple for loop:")
for i in range(5):
    print(i)

# Iterating over a list
print("\nIterating over a list:")
fruits = ["apple", "banana", "cherry"]  # fruits is a list type variable
for fruit in fruits:
    print(fruit)

# Using the range function
print("\nUsing the range function:")
for i in range(1, 10, 2):
    print(i)

# 3. While Loops
print("\nWhile Loops:")

# Simple while loop
print("Simple while loop:")
count = 0
while count < 5:
    print(count)
    count += 1

# 4. Loop Control Statements
print("\nLoop Control Statements:")

# Break statement
print("Break statement:")
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue statement
print("\nContinue statement:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# 5. Nested Loops
print("\nNested Loops:")

# Simple nested loop
print("Simple nested loop:")
for i in range(3):
    for j in range(3):
        print(f"i: {i}, j: {j}")

# 6. Practical Examples
print("\nPractical Examples:")

# Sum of first n natural numbers
n = 10
sum = 0
for i in range(1, n + 1):
    sum += i
print(f"Sum of first {n} natural numbers is: {sum}")

# Factorial of a number
number = 5
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"Factorial of {number} is: {factorial}")

# 7. Exercises
print("\nExercises:")
print("1. Write a program that prints all the even numbers from 1 to 20.")
print("2. Write a program that calculates the sum of all odd numbers from 1 to 50.")
print("3. Write a program that prints a multiplication table for a given number.")
print("4. Write a program that finds the maximum number in a list.")

# Example solution for Exercise 1
print("\nExample solution for Exercise 1:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
