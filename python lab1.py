Python 3.7.3 (default, Apr  3 2019, 05:39:12) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a= 12
>>> b=345
>>> a+b
357
>>> a-b
-333
>>> b-a
333
>>> a*b
4140
>>> a/b
0.034782608695652174
>>> a%b
12
>>> b**a
2843342266303054544082275390625
>>> a^b
341
>>> a**b
2077446682327378559843444695582704973572786912705232236931705903179519704325276892191015329301807037794598378537132233994613616420526484930777273718077112370160566492728059713895917217042738578562985773221381211423961068296308572143393854703167926779929682604844469621152130457090778409728703018428147734622401526422774317612081074841839507864189781700150115308454681772032
>>> 2^2
0
>>> a = [ 1, 2, 3, 5, 'python', 'lab', @ ]
SyntaxError: invalid syntax
>>> a = [ 1, 2, 3, 5, 'python', 'lab', ]
>>> a[3]
5
>>> [1:-1]
SyntaxError: invalid syntax
>>> a[1: -1]
[2, 3, 5, 'python']
>>> 
>>> 
>>> a[-1]
'lab'
>>> len(a)
6
>>> insert a(3, 4)
SyntaxError: invalid syntax
>>> a.insert(3, 4)
>>> a
[1, 2, 3, 4, 5, 'python', 'lab']
>>> a.append('added text')
>>> A
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    A
NameError: name 'A' is not defined
>>> a
[1, 2, 3, 4, 5, 'python', 'lab', 'added text']
>>> a.remove(-1)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.remove(-1)
ValueError: list.remove(x): x not in list
>>> a.remove('added text')
>>> a
[1, 2, 3, 4, 5, 'python', 'lab']
>>> a.pop()
'lab'
>>> a.pop(3)
4
>>> a.pop()
'python'
>>> a
[1, 2, 3, 5]
>>> a.reverse()
>>> a
[5, 3, 2, 1]
>>> a.sort()
>>> a
[1, 2, 3, 5]
>>> a=a.copy()
>>> s
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> s= a.copy()
>>> s
[1, 2, 3, 5]
>>> a.append(100, 100, 100, 100)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.append(100, 100, 100, 100)
TypeError: append() takes exactly one argument (4 given)
>>> a.append(100)
>>> a.append(100)
>>> a.append(100)
>>> a
[1, 2, 3, 5, 100, 100, 100]
>>> a.count(100)
3
>>> a.insert(2,44)
>>> a
[1, 2, 44, 3, 5, 100, 100, 100]
>>> a.insert(2,44,\)
	 
SyntaxError: unexpected character after line continuation character
>>> a= 'this is a string'
>>> a[0]
't'
>>> a.upper()
'THIS IS A STRING'
>>> a.istitle
<built-in method istitle of str object at 0x7f05ebb61390>
>>> a.lower
<built-in method lower of str object at 0x7f05ebb61390>
>>> a.lower()
'this is a string'
>>> a
'this is a string'
>>> a.capitalize()
'This is a string'
>>> a.iscapitalize()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a.iscapitalize()
AttributeError: 'str' object has no attribute 'iscapitalize'
>>> a.title()
'This Is A String'
>>> a.istitle()
False
>>> a
'this is a string'
>>> a= a.title()
>>> a.istitle()
True
>>> b = 'this is another string'
>>> a + b
'This Is A Stringthis is another string'
>>> a= a.title()
>>> 
=============== RESTART: /home/it2016b212/Desktop/program1.py ===============
163
>>> print('TUPLES')
TUPLES
>>> a= ( 1, 2, 3, 4, 5, -6, 'home')
>>> len(a)
7
>>> min(a)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    min(a)
TypeError: '<' not supported between instances of 'str' and 'int'
>>> a = (2, 3, 4, -12. -34 )
>>> min(a)
-46.0
>>> a
(2, 3, 4, -46.0)
>>> a = (12 13, 3, 4, 6)
SyntaxError: invalid syntax
>>> a = (12+ 13, 3, 4, 6)
>>> a
(25, 3, 4, 6)
>>> min(a)
3
>>> max(a)
25
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> 
