'''
We are going to learn different type of functions
Based on the purpose of it:
1] Function only doing some tasks and returning nothing [Even if function returns nothing,it returns "None" by default]
2] Function returning something
Based on the parameters rather parameter types
1] Normal paramters
2] Default value parameters/Optinal parameters [Basically parameters are positional in python if not specified explicitely]
3] asteric paramters
4] double asteric parameters
'''
def function_not_returning_anything():
    print("Body of function that returns nothing: \n\tThis function does not return anything")

print("Lets see what this non returning function produces:",function_not_returning_anything())
print(80*"-")

def function_returning_something_salary(basic_pay,inflation):
    print("Body of function that returns something")
    calculate_salary = basic_pay * inflation
    return calculate_salary

# salary = function_returning_something_salary(2400,7)   We need to save returned value from function execution in a variable so that we can use it.
print("Output by function returning someting(salary): Rs.",function_returning_something_salary(2400,7))
print(80*"-")

# The parameters which are going to have default parameters must be at the end in function declaration
# Even if a function has default parameters we can pass a value in function call to override default one
def function_having_default_parameters(basic_pay, inflation=3):
    print("Function that has default parameters:")
    calculate_salary = basic_pay * inflation
    print(f"Salary calculated : {calculate_salary}")

print("Function execution:",function_having_default_parameters(3400))
print(80*"-")

'''
* - This represents the list of items is passed to this variable and gets stored as tuple in this variable
We need to unpack them if we need and then use it for further use
'''
def function_with_parameters_having_single_asterisk(*name_tuple):
    print("Function with * args")
    print(f"First Name : {name_tuple[0]}")
    print(f"Middle name : {name_tuple[1]}")
    print(f"Last Name : {name_tuple[2]}")

'''
Wrong way :
------------
full_name=['Ghanshyam','Sonyabapu','Bambale']
function_with_parameters_having_single_asterisk(full_name)

ERROR:
    print(f"Middle name : {name[1]}")
IndexError: tuple index out of range
'''
function_with_parameters_having_single_asterisk("Ghanshyam","Sonyabapu","Bambale")
print(80*"-")

'''
**  -   Parameters passed to the variable which has ** as prefix receives a dictionary passed over from function call
function call should have key value parameters passed as like and assignment of parameter name and value ex. key='value' or key=20
'''
def function_with_parameters_having_double_asterisk(**name_dictionary):
    print(name_dictionary)
    print("First Name : ",name_dictionary['first_name'])
    print("Middle Name : ",name_dictionary['middle_name'])
    print("Last Name : ",name_dictionary['last_name'])

function_with_parameters_having_double_asterisk(first_name="Ghanshyam",middle_name='Sonyabapu',last_name="Bambale")
print(80*'-')
