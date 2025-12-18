#python datatype to json using json.dumps() method:

import json
data = {
    "email": "123@gmail.com",
    "username": "mruh"
}

print(type(data))
print(data)
result = json.dumps(data)
print(result)

#json format to python format using json.load() method:

import json
r = json.loads(result)
print(r)