# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@Company.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)     
        
        
emp1=Employee('Raghu','bhai',1000000000)

emp2=Employee('mantu' ,'rumba',0.111111)

print(emp1.email)
print(emp2.email)
print(emp1.fullname())
print('\n')
print(Employee.fullname(emp2))