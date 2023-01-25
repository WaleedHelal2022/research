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

