import random

# Review: Strings and Conditional Statements
greeting = "Hello, World!"
name = 'Alice'
print(greeting + " " + name)
print(f"The length of the full greeting is: {len(greeting + ' ' + name)}")

names = ["adrian", "joey", "tom", "ethan", "jack", "gemma",
         "pete", "hintash", "maryam", "veronica", "amy", "todd"]
idx = random.randint(0, len(names) - 1)
print(f"The name at index {idx + 1} is {names[idx]}")

print(name.upper(), name.lower())

gibberish = "adfhjhsbfjb wjehfjdh puqer jlfkvh aoibfj lawenfihpajsdbf jasndfioew"
print(gibberish.find("dhpu"))

new_greeting = greeting.replace("World", "Everyone")
print(new_greeting)

age = 18
if age >= 18:
    print("You are an adult.")

score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
