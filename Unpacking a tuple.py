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
