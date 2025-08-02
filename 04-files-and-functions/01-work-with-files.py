#!/usr/bin/env python3
f = open ('./text.txt', 'r')

data = f.read()
print (data, '\n')

f.close()
g = open ('./new-text.txt', 'w')
g.write(data + '\nto tell you I\'m sorry')
g.close()
