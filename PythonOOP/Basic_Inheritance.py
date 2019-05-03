# Parent class
class Employee:
    def calculate_salary(self, basic_pay_param, hra_param):
        basic_pay =  basic_pay_param
        hra = hra_param
        travelling_allowance = self.travelling_allowance
        grade_pay = self.grade_pay
        salary =  basic_pay_param + hra + travelling_allowance + grade_pay
        self.salary = salary

# Child class
class Contractors(Employee): # Class Inheritance is acheived by naming the parent class in paranthesis 
    def __init__(self):
        self.employee_name = ""
        self.salary = ""
        self.employement_type = "Contractor"
    
    def create_employee(self, name_param, department_param, travelling_allowance, grade_pay_param):
        self.name = name_param
        self.department = department_param
        self.travelling_allowance = travelling_allowance
        self.grade_pay = grade_pay_param

# Creating object/instance of the child class
employee_ctr_1 = Contractors()
employee_ctr_1.create_employee("Bad Coder","Engineering",5000, 3000)

# Accessing base class's method through child class # Basic Inheritance
employee_ctr_1.calculate_salary(20000,8000)
print("Salary of the employee: {0} is {1}".format(employee_ctr_1.name,employee_ctr_1.salary))

'''
OUTPUT:
----------
Salary of the employee: Bad Coder is 36000
'''