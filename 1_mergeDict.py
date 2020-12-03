Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d1 = {"1":"amith", "2":"neeja"}
>>> d2 = {"3":"kumar", "4":"preethi"}
>>> d3 = {**d1,**d2}
>>> print(d3)
{'1': 'amith', '2': 'neeja', '3': 'kumar', '4': 'preethi'}
>>> 