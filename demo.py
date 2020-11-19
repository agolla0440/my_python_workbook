import json
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))


# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["name"])