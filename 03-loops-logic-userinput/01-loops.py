#!/usr/bin/env python3
# I assume you know what loops are
# so I just write the syntax

# while loops
i = 0
while i < 50:
    print (i)
    i += 1

fruits = ['apple','orange','mango','avocado','melon']
fruits_count = len (fruits)

name_index = 0
while name_index < fruits_count:
    print (name_index)
    print (fruits[name_index])
    name_index += 1

# for loops
for i in range(10):
    print (i)

for fruit in fruits:
    print (fruit)