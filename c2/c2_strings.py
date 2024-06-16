# Creating strings
greeting = "Hello, World!"
# greeting: string type variable; value = "Hello World!"

name = 'Alice'  # string

age = '18'  # string
age_num = 18  # int

# Printing strings
print(greeting)
print(name)

# Concatenation
full_greeting = greeting + " " + name
print(full_greeting)

# Typecasting
# add = '1' + 1  # TypeError: can only concatenate str (not "int") to str
typecasting = str(1)  # int -> string
print(typecasting, type(typecasting))
add2 = '1' + str(12)  # Typecasting
print(add2, type(add2))
age = 19
print("My name is Rafael. I am " + str(age) + " years old")


# String length
name = 'Adam Roberge'
length_name = len(name)
print(length_name)

length = len(full_greeting)
print(length)
print(f"The length of the full greeting is: {length}")
print(f"My name is {name}")

# Indexing
name = 'Sergei Flozov'
index = 3
char = name[index]
print(f"The first character in the name is: {char}")

# Slicing
first_three_chars = name[0:3]  # name[a:b] -> a 는 포함, b 는 포함되지 X
print(f"The first three characters in the name are: {first_three_chars}")
slice_chars = name[3:8]
print(f"The first three characters in the name are: {slice_chars}")

# Negative indexing
last_char = name[-1]
print(f"The last character in the name is: {last_char}")

# Changing case
print(name.upper())
print(name.lower())

# Finding a substring
print(full_greeting)
find_word = "o"
position = full_greeting.find(find_word)
print(f"Position of '{find_word}' in full_greeting: {position}")

# Replacing a substring
new_greeting = full_greeting.replace("World", "Everyone")
print(new_greeting)

# Splitting a string
words = full_greeting.split()
print(words)  # list
