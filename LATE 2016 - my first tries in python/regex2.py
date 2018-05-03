import re

num = re.compile(r'\(\d\d\) (\d\d\d) (\d\d \d\d)')
mo = num.search('ble ble njhsvhihvsohi (59) 811 32 68')
print(mo.group())
#print(mo.group(1))
mo.groups()
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)


