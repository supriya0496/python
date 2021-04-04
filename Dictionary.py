'''
Dictionary is a set of key and value pair
Each key should have a value
Values may repeat but key should alwyas be unique

'''
Di = {'movie': 'jab we met', 'actor': 'Shahid', 'actress':'Kareena'}
print(Di)
Di['Song']= 'Nagada'
print(Di)
Di.pop('Song')
print(Di)


String = input("Enter a string: ")
def palindrome(strn):
    return strn == strn[::-1]
s = palindrome(String)

if s:
    print('Yes')
else:
    print('No')

print("Trying git diff command")
