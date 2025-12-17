int(input("enter number: "))
set1 = {56.2, 'a', 78.9}
print(set1)

list1 = {46.2, 'b', 78.5}
print(list1)

dict1 = {"key1":1, "key2":4}
print(dict1)

dict1 = {"key1":1, "key2":4, "key3":5, "key4":9, "key5":7}
keys = dict1.keys()
print(keys)

dict1 = {"key1":1, "key2":4, "key3":5, "key4":9, "key5":7}
values = dict1.values()
print(values)
list1 = list(values)
print(list1[0])
print(list1[1])

for i in list1:
    print(i)
def add():
    return 23+45
result = add()
print(result)

year = int(input("enter year : "))
current_year = 2055
age = current_year - year
print("your age is", age)

def add(a, b):
    return a + b

print(add(3, 4))
print(add(10, 20))

import requests
data = requests.get("https://en.wikipedia.org/wiki/India")
print(data.text)