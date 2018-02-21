#!/usr/bin/python

# Udacity Model
# https://gist.github.com/chenghan/7456549

# Open file
#https://stackoverflow.com/questions/5214578/python-print-string-to-text-file


import sys
import csv
import re
import codecs

def mapper():
    reader = csv.reader( sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    try:
        for line in reader:
            # Read do BODY field

            if line[0] == '4582':
                print('aqui')

            #words = re.findall(r"[\w']+", line[4])
            words = line[4].split(' ')
            words = map(lambda x: x.lower(), words)
            
            # if "fantastically" in words:
            #     writer.writerow(line)

            for word in words:
                writer.writerow( [line[0], word, 1])

    except Exception as e:
        raise  RuntimeError("Line {0} - Error {1}".format( line[0], str(e)))

# This function allows you to test the mapper with the provided test string
def main():

    # CSV file written with Python has blank lines between each row
    # https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row          
    
    sys.stdin = open('forum_data/forum_node.tsv',encoding="utf8")
    sys.stdout = open('logq7mT.log', 'w', newline='',encoding="utf8")
    
    mapper()

main()            

