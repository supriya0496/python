'''
List has elements that are enclosed within the square brackets
List is used to store multiple values in a single variable
Some of the in-build functions are - len remove append sum min max etc
examples are shown in the List_git program
'''


Number1 = int(input('Enter first number: '))
Number2 = int(input('Enter second number: '))

def add(num1,num2):
    sums = num1 + num2
    print(sums)

def sub(n1,n2):
    minus = n1 - n2
    print(minus)
    
add(Number1,Number2)
sub(Number1,Number2)
