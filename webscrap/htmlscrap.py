import requests, bs4

'''res = requests.get('http://nostarch.com')
try:
    res.raise_for_status()
    noStarchSoup = bs4.BeautifulSoup(res.text)
except Exception as exc:
    print('There was a problem: \s ' % exc)'''

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
elems = exampleSoup.select('#author')

print(elems[0].get_text())
print(str(elems[0]))
print(str(elems[0].attrs))

pElems = exampleSoup.select('p')
print(str(pElems[1].getText()))
