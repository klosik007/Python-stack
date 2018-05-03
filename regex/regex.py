import re

f = open('randomcharacters.txt')

strToSearch =''

for line in f:
    strToSearch+=line

print(strToSearch)

patFinder1 = re.compile('Aa1B')

findPat1 = re.search(patFinder1, strToSearch)

print(findPat1.group())
print(findPat1.start())
print(findPat1.end())
print(findPat1.span())

findPat1 = re.findall(patFinder1, strToSearch)

for i in findPat1:
    print(i)

splitFound = patFinder1.split(strToSearch)
print(splitFound)

subFound = patFinder1.sub('Real Text ', strToSearch)
print(subFound)



