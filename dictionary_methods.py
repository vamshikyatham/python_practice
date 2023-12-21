# Dictionary
# clear
edict = {"name": "vamshi", "roll no": 412, "age": 25}
print(edict)
edict.clear()
print("After clear:", edict)

# Copy
edict = {"name": "vamshi", "roll no": 412, "age": 25}
tdict = edict.copy()
print("After copying from edict to tdict:", tdict)

# get
x = edict.get("name")
print("After getting the value of the key name is 'name':", x)

# Keys
x = edict.keys()
print("To know the only keys of the dictionary,return as a list:", x)

# values
x = edict.values()
print("To know the only values of the dictionary, return as a list:", x)

# Items
x = edict.items()
print("Returns a list containing a tuple for each key value pair:", x)

# Update
edict.update({"gender": "male"})
print("After updating a new key and value to the dictionary:", edict)

# pop
edict.pop("age")
print("After popping thr age from the dictionary:", edict)

# popitem
edict.popitem()
print("After popitem means removes the last pair in dictionary:", edict)

# From keys
x = ("key1", "key2", "keys")
y = 1
tdict = dict.fromkeys(x, y)
print(tdict)
