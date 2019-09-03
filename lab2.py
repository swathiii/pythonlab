Python 3.7.3 (default, Apr  3 2019, 05:39:12) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = { 'name' : 'swathi', 'age' : 20, 'course' : 'engineering' }
>>> print(a)
{'name': 'swathi', 'age': 20, 'course': 'engineering'}
>>> a['age'] = 21
>>> print(a)
{'name': 'swathi', 'age': 21, 'course': 'engineering'}
>>> b = {
'student1':{
	'name': 'swathi',
	'age': 20,
	'course': 'engineering',
	'fee': 85000,
},
'student2': {
	'name':'sam',
	'age':21,
	'course':'bcom',
	'fee': 34000,
},
'student3':{
	'name':'tom',
	'age':24,
	'course': 'MBA',
	'fee':3400000,
}
}
>>> for 'student2' in b:
	print( b['student2'])
	
SyntaxError: can't assign to literal
>>> print(b['student1'])
{'name': 'swathi', 'age': 20, 'course': 'engineering', 'fee': 85000}
>>> print(b['student3'])
{'name': 'tom', 'age': 24, 'course': 'MBA', 'fee': 3400000}
>>> del b['student3']
>>> print(b)
{'student1': {'name': 'swathi', 'age': 20, 'course': 'engineering', 'fee': 85000}, 'student2': {'name': 'sam', 'age': 21, 'course': 'bcom', 'fee': 34000}}
>>> print(a)
{'name': 'swathi', 'age': 21, 'course': 'engineering'}
>>> a.pop('course')
'engineering'
>>> print(a)
{'name': 'swathi', 'age': 21}
>>> a.popitem()
('age', 21)
>>> print(a)
{'name': 'swathi'}
>>> 
