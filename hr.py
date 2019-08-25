"""
This is a simple example of how oop works in Python
whit Model class hierarchies using inheritance

Inheritance models what is called an is a relationship. 
This means that when you have a Derived class that inherits 
from a Base class, you created a relationship where Derived 
is a specialized version of Base

"""


# Interface
# PayrollSystem class that processes payroll
class PayRollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} -- {employee.name}')
            print(f'--> Check amount: {employee.calculate_payroll()}')
            print('')
