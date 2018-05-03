import re

f = open('websites.txt')

strToSearch = ''
for line in f:
    strToSearch+=line

httpregex = re.compile(r'''
       (\w{4})
''')

https = httpregex.findall((strToSearch))
print(https)