#!/usr/bin/env python3
# Dictionaries are datatypes that contain one or more key-value pairs of data.

Me = {
    'name' : 'Ali Aryani'
    , 'github' : 'aliaryani-security'
    , 'instagram' : 'aliaryani.security'
}

# to add something to it :
Me["X"] = "aliaryani_sec"
print (Me)
# changing a value is the same as this, just provide the key

# to access a value of it:
print (Me['name'])

# access the keys:
print (Me.keys())

# access the values:
print (Me.values())