# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 21:33:13 2017

@author: koduri Raghvendra ra
"""

class Employee:
    raise_amount=1.04
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@Company.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)     
    def apply_raise(self):
       self.pay=int(self.pay*self.raise_amount)
    def __repr__(self):
        return "Employee({} ,{},{})".format(self.first,self.last,self.pay)
    def __str__(self):
       return "{} - {}".format(self.fullname(),self.email) 
    def __add__(self,relg):
       return self.pay+relg.pay
    def __len__(self):
        return len(self.fullname())
       
emp1=Employee('Raghu','bhai',100)

emp2=Employee('mantu' ,'rumba',0.111111)
print(emp1+emp2)
print(emp1.__add__(emp2))
print(emp1.__repr__())
print(emp1.__str__())       
print(int.__add__(2,3))
print(emp1.__len__())
print(len(emp1))