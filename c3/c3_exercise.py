# Even Numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# Sum of All Odd Numbers from 1 to 50
sum = 0
for i in range(1, 51):
    if i % 2 != 0:
        sum += i
print(f"Sum of all odd numbers from 1 to 50 is: {sum}")


# Multiplication Table
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# Find the Maximum Number in a List
numbers = [3, 7, 2, 8, 4, 10, 5]
max_number = numbers[0]
for num in numbers:
    if num > max_number:
        max_number = num
print(f"The maximum number in the list is: {max_number}")
