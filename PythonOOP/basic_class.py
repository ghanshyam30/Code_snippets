class Student: # c should not be capital but class name should be in Camel case
    #Attributes
    # Class variable
    school_name = "Bad Coding Academy"  # can be treated as constant

    # Behaviour / Methods
    def marks(self, name, maths, science):
        # Instance variables always referenced with self/instance.
        self.name = name
        self.math_marks = maths
        self.science_marks = science
    
    def show_report(self):
        total = self.math_marks + self.science_marks
        print("Total for {0}:{1}".format(self.name,total))
    
#Creation of the object
student1 = Student()

#Calling a method using object
student1.marks("Alen",59,99)
student1.show_report()

#Creation of 2nd object
student2 = Student()
student2.marks("Bob",66,86)
student2.show_report()

# Accessing the class variable using object
print("School Name:",student1.school_name)

# Other way to access class variable using Class name itself
print("School Name:",Student.school_name)

# Updating the class variable
Student.school_name = "Good Coding Academy"
# Reprint after changing the class variable
print("School Name:",Student.school_name)

# Update class variable for single object
student1.school_name = "Bad Coding Academy"
# Accessing the class variable using object 
print("School Name:",student1.school_name)

# Changing class variable for one object wont alter the class variable for other objects
# Accessing the class variable using object
print("School Name:",student2.school_name)

'''
OUTPUT
-----------
Total for Alen:158
Total for Bob:152
School Name: Bad Coding Academy
School Name: Bad Coding Academy
School Name: Good Coding Academy
School Name: Bad Coding Academy
School Name: Good Coding Academy
'''
