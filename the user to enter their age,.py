# Description: his code prompts the user to enter their age, and then prints a message based on the age. If the age is less than 18, the message is "You are a minor." If the age is greater than or equal to 18 and less than 60, the message is "You are an adult." If the age is greater than or equal to 60, the message is "You are a senior citizen."


age = int(input("What is your age? "))

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
