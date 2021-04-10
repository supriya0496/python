def marks():
    num = int(input("Enter the marks obtained: "))
    if num >= 80:
        print("Distinction")
    elif num>=60 and num<=70:
        print("Average")
    elif num>=50 and num<60:
        print("Below Average")
    else:
        print("Fail")

def palin():
    string = input("Enter the string: ")
    res = string[::-1]
    if res:
        print("yes")
    else:
        print("no")
    
a = int(input("Enter 0 or 1: "))

if a == 1:
    marks()
else:
    palin()
