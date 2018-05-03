import csv, os

os.makedirs('headerRemoved', exist_ok=True) #make 'headerRemoved' folder

#loop through files in directory
for csvFileName in os.listdir('.'):
    if not csvFileName.endswith('.csv'):
        continue

    print('Removing header from ' + csvFileName + '...')

#Read the CSV file in (skipping first row)
csvRows = []
csvFileObj = open(csvFileName)
readerObj = csv.reader(csvFileObj)
for row in readerObj:
    if readerObj.line_num == 1:
        continue
    csvRows.append(row)

csvFileObj.close()

#Write to CSV file
csvFileObj = open(os.path.join('headerRemoved', csvFileName), 'w', newline='')
csvWriter = csv.writer(csvFileObj)
for row in csvRows:
    csvWriter.writerow(row)
csvFileObj.close()