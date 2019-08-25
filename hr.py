"""
This is a simple example of how oop works in Python
whit Model class hierarchies using inheritance

Inheritance models what is called an is a relationship. 
This means that when you have a Derived class that inherits 
from a Base class, you created a relationship where Derived 
is a specialized version of Base

"""
from abc import ABC, abstractclassmethod


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


# base class 
# Employee that handles the common interface for every employee type
class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractclassmethod
    def calculate_payroll(self):
        pass

# derived class
# SalaryEmployee that inherits Employee
class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


# derived class
# HourlyEmployee that inherits Employee
class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hours_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hours_rate = hours_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hours_rate


# derived class
# CommissionEmployee that inherits SalaryEmployee
class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


# This class doesn't derive from Employee
# But it exposes the same Interface
# required by PayRollSystem
class DisgruntledEmployee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_payroll(self):
        return 10000