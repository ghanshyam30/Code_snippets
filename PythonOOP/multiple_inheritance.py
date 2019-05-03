class A:
    def random1(self):
        print("Hi, You got into second Superclass too")

class B():     
    def random2(self):
        print("Great, you got into 1 st superclass")

class C(B,A): #Class C inherits class B and class A wherein Class B has hier precedence than class A i.e left first
    def random3(self):
        self.random2()      #Notice you can not call superclass methods without the "self" instance
        self.random1()

# Instance creation of class C
class_c_object = C()
# Calling method of class C, which in turn will access members of class B and class A via inheritance
class_c_object.random3()

'''
OUTPUT-
---------------
Great, you got into 1 st superclass
Hi, You got into second Superclass too
'''