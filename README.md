# research
Research Repository
Python Code Examples
This repository contains several examples of Python code, including:
•	Using the if and elif statements to check a user's input
•	Using a function to replace the user input
•	Using a function that returns a tuple
•	Using a function that returns a tuple based on user input
•	Using a simple calculator program that adds two numbers
•	Using password generator
•	Using Employee Ticket Counter
•	Using how to use a for loop
•	Using generates a random ticket number
•	Using Factorial Calculator
•	Using the check if a number is even or odd
Getting Started
To run the code examples, you will need to have Python installed on your system. You can download the latest version of Python from the official website (https://www.python.org/downloads/).
Example 1: Using the if and elif statements to check a user's input
The first example shows how to use the if and elif statements to check a user's input and determine if the number is positive, negative, or zero. It prompts the user to enter the number and uses the input function to get the user input.
#   1. Write a program that asks the user for a score.
#   2. If the score is greater than or equal to 90, print "Grade A".
#   3. If the score is greater than or equal to 80, print "Grade B".
#   4. Otherwise, print "Grade C".
#   5. If the score is greater than or equal to 94, print "Excellent!".
#   6. Otherwise, print "Good Job!".
score = int(input("What is your score? "))

if score >= 90:
    print("Grade A")
    if score >= 94:
        print("Excellent!")
    else:
        print("Good Job!")
elif score >= 80:
    print("Grade B")
else:
    print("Grade C")

Example 2: Using a function to replace the user input
The second example shows how to use a function to replace the user input. It defines a function get_age() which returns a hardcoded age, instead of prompting the user for input.
# Description: his code prompts the user to enter their age, and then prints a message based on the age. If the age is less than 18, the message is "You are a minor." If the age is greater than or equal to 18 and less than 60, the message is "You are an adult." If the age is greater than or equal to 60, the message is "You are a senior citizen."


age = int(input("What is your age? "))

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

Example 3: Using a function that returns a tuple
The third example shows how to use a function that returns a tuple. It defines a function get_employee_info() which returns a tuple containing the name, age, and salary of an employee.
# Description: Unpacking a tuple

def get_employee_info():
    name = "Waleed"
    age = 25
    salary = 1000
    return name, age, salary

employee_info = get_employee_info()

print("Name: ", employee_info[0])
print("Age: ", employee_info[1])
print("Salary: ", employee_info[2])

Example 4: Using a function that returns a tuple based on user input
The fourth example shows how to use a function that returns a tuple based on user input. It defines a function get_employee_info() which prompts the user for input and returns a tuple containing the name, age, and salary of an employee.
# Description: This program will ask the user for the name, age, and salary of an employee. It will then print the information back to the user.

def get_employee_info():
    name = input("Please enter the employee's name: ")
    age = int(input("Please enter the employee's age: "))
    salary = float(input("Please enter the employee's salary: "))
    return name, age, salary

employee_info = get_employee_info()

print("Name: ", employee_info[0])
print("Age: ", employee_info[1])
print("Salary: ", employee_info[2])

Example 5: Using a simple calculator program that adds two numbers
The code defines a function add(a, b) which takes in two arguments a and b and returns their sum using the + operator.
It then calls the function with the values 3 and 4 and assigns the returned value to a variable result and then prints the result.
# Description: This program is a simple calculator that adds two numbers

def add(a, b):
    return a + b

print(add(3, 4)) # prints 7

Example 6 password generator
This program generates a password of a fixed length of 11 characters, made up of a combination of lowercase and uppercase letters, numbers, and special characters. The while loop is used to execute the code inside it, and the quit() function is used to exit the program after the password is generated.
# Description: Password Generator

import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ1234567890"

while 1:
    password_len = int(11)
    password_count = int(1)
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Here is your password : ", password)

    quit()

Example 8 Employee Ticket Counter
The code defines a class Employee which contains a class variable counter that is set to 2000. It also defines an __init__ method that takes in 3 arguments: empTick, empNo, and empName.The __init__ method assigns the input values to the corresponding class variables, assigns the class variable counter to empTick, and then increments the class variable counter by 1.After that the program prompts the user to enter their ID and name, and assigns them to the variables empNo and empName respectively.Finally, the program displays a message that the ticket has been submitted successfully and displays the value of the counter which is the employee's ticket number.
# Description: Employee Ticket Counter
#           The program should generate a random number between 1000001 and 1999999
#           and assign it to the employee ticket.
#        The program should also generate a counter that starts at 2000 and increments
#           by 1 for each ticket submitted.
#        The program should display the employee ticket and the counter.
#

class Employee:
    counter = 2000

    def __init__(self, empTick, empNo, empName):
        self.empNo = empNo
        self.empName = empName
        self.empTick = empTick
        self.empTick = Employee.counter
        Employee.counter += 1



empNo = int ( input ( "Enter Stuff ID : " ) )
empName = str ( input ( "Enter your Name : " ) )
print ( "Your Ticket has been submitted successfully" )
print ( "Your Ticket Number is : ", Employee.counter )
 

Example 9 how to use a for loop
This code uses a for loop to iterate through a range of numbers from 0 to 4 (as range(5) generates numbers from 0 to 4), and for each iteration, it prints the current value of the variable i.
The for loop is used to iterate over a sequence of numbers (in this case, generated by the range(5) function), and for each iteration, the current value of the loop variable (i) is printed to the console using the print() function.This code is a simple example of how to use a for loop in Python. It prints the numbers 0,1,2,3,4 to the console.You can use this code as a reference and add more functionality, like doing some operations on each iteration or creating a more complex range of numbers.
# Description: This is a simple program that prints the numbers 0 to 4. It is a good example of how to use a for loop.

for i in range(5):
    print(i)

Example 10 generates a random ticket number
The code imports the random module and defines a string of characters that are used to generate the ticket number. It then uses a while loop to prompt the user for the desired ticket number length and number of tickets to generate.Inside the while loop, it uses a for loop to generate the number of tickets.For each iteration of the loop, it creates an empty string TicketId and then uses another for loop to iterate for the desired length of the ticket number. Inside this inner loop, it selects a random character from the chars string, and appends it to the TicketId string.Finally, it prints the generated ticket number.
# Description: This program generates a random ticket number

import random
chars = "1234567890"

while 1:
    Ticket_len = int(10)
    Ticket_count = int(1)
    for x in range(0, Ticket_count):
        TicketId = ""
        for x in range(0, Ticket_len):
            Ticket_char = random.choice(chars)
            TicketId = TicketId + Ticket_char
        print("Here is your TicketId : ", TicketId)

    quit()

Example 12 Factorial Calculator
The code defines a function factorial(n) which takes in a number as an argument. The function uses an if-else statement to check if the input number is 0. If it is, it returns 1, else it returns the input number multiplied by the factorial of the input number minus 1.It then assigns the value 5 to a variable num and calls the factorial(num) function with the num as an argument and assigns the returned value to a variable result.Finally, it prints the result of the factorial calculation along with the input number.
# This is a Python script that calculates the factorial of a given number.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = 5
print("The factorial of", num, "is", factorial(num))

Example 13 check if a number is even or odd
The code defines a function to check check if a number is even or odd A number that is divisible by 2 and generates a remainder of 0 is called an even number. All the numbers ending with 0, 2, 4, 6, and 8 are even numbers. On the other hand, number that is not divisible by 2 and generates a remainder of 1 is called an odd.Finally, it prints the result of the check if a number is even or odd along with the input number.
#Description:  This is a Python script that uses a if statement to check if a number is even or odd

num = 3
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))



Running the code
You can run the code examples by using the command prompt and typing python <filename>.py and hit enter.
For example, to run the first example, you would type python example1.py and hit enter.
Note
Please make sure to replace the <filename> with the actual name of the file you want to run.
Please also note that these are just examples and you can use them as a reference to build your own Python projects.
Conclusion
These examples demonstrate different ways to work with Python, and how to use if-elif statements, functions, and tuples. You can use the examples provided here as a starting point for your own projects, and modify them to suit your needs.

