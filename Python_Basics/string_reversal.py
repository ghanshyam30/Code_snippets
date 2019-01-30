'''
This file is created with the intension of getting to know what are the various ways trough which we can deliver the reversed for of given string.
'''
# Importing the library required for computing the time of execution of different functions or statements or computations
import timeit  
class Slicing():
    input_string = "TheBadCoder"
    #1 - By Slicing
    def by_slicing(self, string_param):
        # Apply slicing and return the reversed sequence
        return string_param[::-1]
    
    #2 - By using inbuilt method reversed and join
    def by_reversed(self, string_param):
        return ''.join(reversed(string_param))
    
    #3 - By using 

    #4 - Printing the results
    def print_result(self, result_to_print):
        print "Result:",result_to_print

input_string = "TheBadCoder"
object1 = Slicing()
result=object1.by_slicing(input_string)
object1.print_result(result)
result=object1.by_reversed(input_string)
object1.print_result(result)

'''
Now we will see what is the execution time consumed by the functions above.
'''
def check_execution_speed(input_string):
    obj2 = Slicing()
    result = timeit.repeat(lambda: obj2.by_slicing(input_string*10))
    print "Time taken by slicing:",result
    result = timeit.repeat(lambda: obj2.by_reversed(input_string*10))
    print "Time taken by reversed:",result

check_execution_speed(input_string)

'''
Output:
------------------
Result: redoCdaBehT
Result: redoCdaBehT
Time taken by slicing: [1.9651814251440747, 2.0325299338794385, 2.1670003912535005]
Time taken by reversed: [11.951109952473578, 12.51488192634962, 12.529698786004811]
'''
'''
---------------------------------------------------------
Conclusion: Slicing is much faster than other two techniques
----------------------------------------------------------
'''