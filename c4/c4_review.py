import random

# Review: Strings and Conditional Statements
greeting = "Hi, how are you doing today? My name is"
name = 'Adrian'
print(greeting + " " + name)
print("The length of the full greeting is: {len(greeting + ' ' + name)}")
print(f"The length of the full greeting is: {len(greeting + ' ' + name)}")

names = ["adrian", "joey", "tom", "ethan", "jack", "gemma",
         "pete", "hintash", "maryam", "veronica", "amy", "todd"]
idx = random.randint(0, len(names) - 1)
print(f"The name at index {idx + 1} is {names[idx]}")

print(name.upper(), name.lower())

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vulputate varius massa eu suscipit. Sed nec finibus lacus. Fusce accumsan dui magna, vitae accumsan ipsum maximus sed. Proin et pretium ligula, ac lobortis dolor. Vivamus ut dui in justo facilisis venenatis et eu turpis. Mauris ut nibh mauris. Pellentesque sollicitudin lectus in dolor egestas, hendrerit lobortis leo pulvinar. Nam id risus arcu. Fusce a consectetur leo. Duis malesuada elementum pellentesque. Morbi lorem quam, efficitur ac mi quis, dignissim rutrum urna. Donec at dictum odio. Morbi massa sapien, luctus nec pretium at, accumsan interdum ligula. Sed eleifend pharetra massa vitae pretium. Curabitur tempus nisi odio, nec molestie lacus elementum non. Nunc ut mi non est rhoncus elementum."
print(lorem.find("dhpu"))
print(lorem.find("maximus"))

new_greeting = greeting.replace("today", "these days")
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
