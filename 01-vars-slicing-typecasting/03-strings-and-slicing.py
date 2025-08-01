#!/usr/bin/env python3
# unlike low level languages,
# strings are not a nightmare here!

# let's write an <a> html tag 
tag = '<a href="https://github.com/aliaryani-security">Github page</a>'
# as you can see, using single quote or double quote
# does not matter, they both can do the job
# but be careful not to ruin your own code !
# in the example above, we cannot use double
# quotes, since we have a pair of double quotes
# right in the middle of our string! in href value

# let us do some slicing now 
url = tag[9:46]
print (url)
# see? it means select characters from 9 to 46 from tag
# this is called slicing

# let's make it more interesting
# index() will help us find that 9 and 46 without any problems

start = "http"
end = '">'

url2 = tag[tag.index(start) : tag.index(end)]
print (url2)
# see? that's better