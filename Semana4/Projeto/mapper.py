import sys
import csv
import time

def mapper():
    first_line = True
    unit_idx = 0
    entries_idx = 0

    try:
        reader = csv.reader(sys.stdin, delimiter=',')
        writer = csv.writer(sys.stdout, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for line in reader:
            if first_line:
                first_line = False
                headers = line
                unit_idx = headers.index("UNIT")
                entries_idx = headers.index("ENTRIESn_hourly")
            else:
                key = line[unit_idx]
                value = line[entries_idx]
                writer.writerow([key, value])

    except Exception as e:
        raise RuntimeError("Reason %s" % str(e))
            
data_Directory = "data"     

# CSV file written with Python has blank lines between each row
# https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row          
sys.stdin = open(data_Directory + '/turnstile_data_master_with_weather.csv')
sys.stdout = open(data_Directory + '/mapper_result1.txt', 'w', newline='')
mapper()