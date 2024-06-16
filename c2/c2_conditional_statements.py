# Simple if statement
age = 19
if age >= 18:  # True
    print("You are an adult.")

# If/else statement
temperature = 25
if temperature > 30:
    print("It's a very hot day.")
elif temperature > 20:  # if 20 < temp <= 30
    print("It's a hot day.")
else:  # if temp <= 20
    print("It's a cool day.")

# If/elif/else statement
score = 78
if score >= 90:  # 90 ~
    print("Grade: A")
elif score >= 80:  # 80 ~ 89
    print("Grade: B")
elif score >= 70:  # 70 ~ 79
    print("Grade: C")
elif score >= 60:  # 60 ~ 69
    print("Grade: D")
else:  # -inf ~ 59
    print("Grade: F")

# Comparison operators -> return boolean (True, False)
x = 10  # variable = value -> store the value in the variable
y = 20
print(x == y)  # False
print(type(x == y))
print(x != y)  # True
print(x < y)   # True
print(x > y)   # False
print(x <= y)  # True
print(x >= y)  # False

a = 1
b = 'abc'
c = "abc"
print(b == c)
print(a == 1)

# in
text = "AUFodihfaoihAPIOHPHDifdjbajbneijBBOFBodnflkanefobadjgoiasheop"
find = "PHDadsfljia;fdie"
if find in text:
    print(True)
else:
    print(False)
