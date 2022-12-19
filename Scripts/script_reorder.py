import csv

def read_csv (filename):
    with open(filename) as incsv:
       reader = csv.DictReader(incsv, delimiter=',')
       for r in reader:
           yield r

columns = ['filePathInUpload', 'expectedTranscription', 'evaluationWeight']

with open('words_file.csv', 'w',newline='') as f:
    writer = csv.DictWriter(f, columns, extrasaction='ignore', delimiter=',')
    writer.writeheader()

    for row in read_csv('sorted.csv'):
        # write row (using the order specified in columns)
        row['evaluationWeight'] = 1
        #uncomment this if you only want filename // else commented
        split_text = row['filePathInUpload'].split(':')
        row['filePathInUpload'] = split_text[1] + "/" + split_text[-1]
        row['expectedTranscription'] = row['expectedTranscription'].replace(" ", "")
        del(row['trial'])
        writer.writerow(row)