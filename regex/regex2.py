import re, pyperclip

f = open('randomcharacters.txt')

strToSearch=''

for line in f:
    strToSearch+=line

print(strToSearch)

patFinder2 = re.compile('\([0-9]{2}\)\s[0-9]{3}\s[0-9]{2}\s[0-9]{2}', re.IGNORECASE)
findPat2 = re.findall(patFinder2, strToSearch)

for i in findPat2:
    print(i, end='')
'''
if(findPat2):
    print(findPat2.group())
else:
    print('Nothing found')'''


