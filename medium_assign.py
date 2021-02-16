'''

This file contains the functions that you need for completing this assignment. 

1. expression_1() --> 30%
2. expression_2() --> 40%
3. expression_3() --> 30% 

Failure to follow the variable name guides will lead to reduction of 10 points. 

DO NOT EDIT THE FUNCTION NAMES.


'''

def expression_1(x):

    print(f"Value x: {x}")
    return x**3 - ((2*x) + (x*x)) - 100 



def expression_2(x, y):

    print(f"Value x: {x}")
    print(f"Value y: {y}")
    return (x**4 / 2*y) - (3*x*y) + (6*y / 7*x)



def expression_3(x, y):
    
    print(f"Value x: {x}")
    print(f"Value y: {y}")
    return ((x**3) + (y*y)) / ((x*x) - (y**3))








if __name__ == "__main__":
    
    result = expression_1(10)
    print(f"The result is : {result}")


    result = expression_2(10,5)
    print(f"The result is: {result}")


    result = expression_2(10,5)
    print(f"The result is: {result}")