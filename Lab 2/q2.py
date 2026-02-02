class Employee:
    name=""
    emp_id=0
    def __init__(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id
    
class FullTimeEmployee(Employee):
    monthly_salary=0
    def __init__ (self,name,emp_id,monthly_salary):
         self.name=name
         self.emp_id=emp_id
         self.monthly_salary=monthly_salary
    def calculate_salary(self):
        return self.monthly_salary
        
class PartTimeEmployee(Employee):
    hours_worked=0
    hourly_rate=0
    def __init__ (self,name,emp_id,hours_worked,hourly_rate):
         self.name=name
         self.emp_id=emp_id
         self.hours_worked=hours_worked
         self.hourly_rate=hourly_rate
    def calculate_salary(self):
        return self.hours_worked*self.hourly_rate


p=PartTimeEmployee("Aamna", 695, 7,90 )
f=FullTimeEmployee("Laiba", 644,15000)
print("Salary of part-time : " ,p.calculate_salary())
print("Salary of full-time : ",f.calculate_salary())
