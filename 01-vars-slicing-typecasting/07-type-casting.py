#!/usr/bin/env python3
# simply, typecasting means 
# converting one type to another
# I write thee examples,
# thee shall read and think

num_a = "62"
num_b = "73"
print (num_a + num_b) # 6273
print (type(num_a), type(num_b))
# both are strings
new_value = int(num_a) + int(num_b)
print (new_value)
print (type(new_value))
# and to finish the topic 
print (type(str(new_value)))
