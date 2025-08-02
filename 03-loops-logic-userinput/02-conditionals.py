#!/usr/bin/env python3

age = int (input("How old are you? "))

if age < 16:
    print ('go play with your toys child!')
elif 16 <= age < 18 :
    print ('still young, aren\'t you?')
elif 18 <= age < 30:
    print ("growing up...")
elif 30 <= age < 45 :
    print ("getting old...")
else:
    print ('respect')