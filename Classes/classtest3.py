# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 19:40:26 2017

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
class Developer(Employee):
  raise_amount=1.10
  def __init__(self,first,last,pay,prog_lang):
      super().__init__(first,last,pay)
      self.prog_lang=prog_lang
      #Employee.__init__(self,first,last,pay)
class Manager(Employee):
  raise_amount=1.10
  def __init__(self,first,last,pay,employees=None):
      super().__init__(first,last,pay)
      if employees is None:
          self.employees=[]
      else:
          self.employees=employees
  def add_emp(self,emp):
      if emp not in self.employees:
          self.employees.append(emp)
          
  def remove_emp(self,emp):
       if emp in self.employees:
           self.employees.remove(emp)
                  
  def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())
      
      #Employee.__init__(self,first,last,pay)

        
emp1=Developer('Raghu','bhai',100,'python')

emp2=Developer('mantu' ,'rumba',0.111111,'java')
k=[]
mgr1=Manager('Sue','Smith',90000,k)
print(mgr1.email)
mgr1.add_emp(emp2)
mgr1.print_emps()
print(issubclass(Manager,Developer))
print(isinstance(mgr1,Developer))

#print(emp2.email)
#print(emp1.fullname())
#print('\n')
#print(Developer.fullname(emp2))
#print(emp1.pay)
#emp1.apply_raise()
#print(emp1.pay)
print(help(Developer))
print(Employee.__dict__)