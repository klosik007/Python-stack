import csv

exFile = open(r'E:\Studia\rok 4\praca inz\pomiary opory\Kłos_P\keller 25_20\Q=0.csv')
exReader = csv.reader(exFile)
for row in exReader:
    print('Row #' + str(exReader.line_num) + ' ' + str(row))

outFile = open('output.tsv', 'w', newline='')
outWriter = csv.writer(outFile, delimiter='\t', lineterminator='\n\n')
outWriter.writerow(['kol1', 'kol2', 'kol3'])
outWriter.writerow(['Hello, Python!', 'eggs', 'just cause'])
outWriter.writerow(['Another spam', 'bacon', 'Trump'])
outFile.close()