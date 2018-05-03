import re

f = open('dates.txt')

strToSearch=''

for line in f:
    strToSearch+=line


datesregex1 = re.compile(r'''(
        (\d[1-12]*)
        (/|-)
        (\d[1-31]*|\d{2})
        (/|-)
        (\d{4}|\d{2})
)''', re.VERBOSE)

datesregex2 = re.compile(r'''(
    (\d{2})
    (/|-)
    (\d[1-31]*)
    (/|-)
    (\d{4})
)''')

datesregex3 = re.compile(r'''(
    (\d{4})
    (/|-)
    (\d{2})
    (/|-)
    (\d{2})
)''')

exactdate = re.compile(r'\d[1-31]\.\d[1-12]\.\d{4}')

dates1 = datesregex1.findall(strToSearch)
print(dates1)

newdates = []





