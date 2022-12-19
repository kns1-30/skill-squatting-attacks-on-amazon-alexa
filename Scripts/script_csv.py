import csv
fn = 'sorted.txt'

columns = ['trial','evaluationWeight','expectedTranscription','filePathInUpload']
csv_fn = 'sorted.csv'
with open(fn, 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)

    with open(csv_fn, 'w',newline='') as out_file:
        writer = csv.writer(out_file, columns, delimiter=',')
        writer.writerow(columns)
        writer.writerows(lines)