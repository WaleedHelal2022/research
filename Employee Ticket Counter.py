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