# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 18:41:44 2017

@author: koduri Raghvendra ra
"""

class Employee:
    raise_amount=1.04
    num_of_emp=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@Company.com'
        Employee.num_of_emp+=1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)     
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount=amount
        
    @classmethod
    def from_string(cls,emp_str):
         first,last,pay=emp_str.split('-')
         return cls(first,last,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        else:
            return True
print(Employee.num_of_emp)        
emp1=Employee('Raghu','bhai',1000000000)
print(emp1.num_of_emp)
emp2=Employee('mantu' ,'rumba',0.111111)
print(Employee.num_of_emp)
print(Employee.raise_amount)
Employee.set_raise_amt(1.05)
print(emp1.raise_amount)
print(emp2.raise_amount)
emp_str_1='Jhon-Doe-70000'
new_emp_1=Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)
import datetime
my_date=datetime.date(2016,7,11)
print( Employee.is_workday(my_date))

#emp1.raise_amount=1.05
#print(emp1.raise_amount)
#emp1.apply_raise()
#print(emp2.raise_amount)
#print(Employee.raise_amount)
#print(emp1.__dict__)
#print(Employee.__dict__)
