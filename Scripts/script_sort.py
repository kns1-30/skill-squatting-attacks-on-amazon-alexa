fn = 'at2G.log'
sorted_fn = 'sorted.txt'

with open(fn,'r') as first_file:

    rows = first_file.readlines()
    try:
        sorted_rows = sorted(rows, key=lambda x: x.split(',')[2], reverse=False)
        with open(sorted_fn,'w') as second_file:
            for row in sorted_rows:

                    second_file.write(row)
    except:
        pass