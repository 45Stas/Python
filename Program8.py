Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> spisok_stud = ["Лена", "Катя"]
>>> spisok_stud.append("Никита")
>>> prin(spisok_stud)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    prin(spisok_stud)
NameError: name 'prin' is not defined
>>> print(spisok_stud)
['Лена', 'Катя', 'Никита']
>>> spisok_stud.extend(["Еркебулан", "Кирилл"])
>>> print(spisok_stud)
['Лена', 'Катя', 'Никита', 'Еркебулан', 'Кирилл']
>>> spisok_stud.insert(1, "Стас")
>>> print(spisok_stud)
['Лена', 'Стас', 'Катя', 'Никита', 'Еркебулан', 'Кирилл']
>>> spisok_stud.append("Рома")
>>> print(spisok_stud)
['Лена', 'Стас', 'Катя', 'Никита', 'Еркебулан', 'Кирилл', 'Рома']
>>> spisok_stud.append("Катя")
>>> spisok_stud.count
<built-in method count of list object at 0x000002094AF7CD88>
>>> spisok_stud.count("Катя")
2
>>> spisok_stud.pop(2)
'Катя'
>>> print(spisok_stud)
['Лена', 'Стас', 'Никита', 'Еркебулан', 'Кирилл', 'Рома', 'Катя']
>>> 
