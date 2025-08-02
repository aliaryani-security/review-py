#!/usr/bin/env python3

# a list is a datatype with one or more vars and an indexed order
months = ['January', 'Fabruary', 'March']
print (type(months))

# let's try finding the index
print (months.index("March"))

# Lists are easy to edit:
months.append("April")
print (months)
months.remove("March")
print (months)

# to see the length of a list:
print (len(months))