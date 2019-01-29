Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> family = ['Father','Mother','Brother','Sister']
>>> family[1]
'Mother'
>>> family
['Father', 'Mother', 'Brother', 'Sister']
>>> family[-2]
'Brother'
>>> family[2]
'Brother'
>>> 'Galle'[3]
'l'
>>> 'Galle'[4]
'e'
>>> family +['dog','cat']
['Father', 'Mother', 'Brother', 'Sister', 'dog', 'cat']
>>> family
['Father', 'Mother', 'Brother', 'Sister']
>>> nunbers = [1,2,3,4,5,6]
>>> numbers = [1,2,3,4,5,6]
>>> numbers
[1, 2, 3, 4, 5, 6]
>>> numbers.append[7,8]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    numbers.append[7,8]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> numbers.append[7]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    numbers.append[7]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> numbers.append(7)
>>> numbers
[1, 2, 3, 4, 5, 6, 7]
>>> numbers.append(7,8,9)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    numbers.append(7,8,9)
TypeError: append() takes exactly one argument (3 given)
>>> numbers[2]= 10
>>> numbers
[1, 2, 10, 4, 5, 6, 7]
>>> numbers[:4]
[1, 2, 10, 4]
>>> numbers[1:4]
[2, 10, 4]
>>> numbers[:3]=[0:0]
SyntaxError: invalid syntax
>>> numbers[:3]=[0,0]
>>> numbers
[0, 0, 4, 5, 6, 7]
>>> numbers[:4]=[1,1]
>>> numbers
[1, 1, 6, 7]
>>> numbers[:2]= []
>>> numbers
[6, 7]
>>> 
