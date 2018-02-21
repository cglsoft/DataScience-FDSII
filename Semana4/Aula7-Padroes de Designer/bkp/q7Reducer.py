#!/usr/bin/python
"""
Your mapper function should print out 10 lines containing longest posts, sorted in
ascending order from shortest to longest.
Please do not use global variables and do not change the "main" function.
"""
import sys


def reducer():

    old_word = None
    doc_ids = []
    total_count = 0

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        
        if len(data_mapped) != 2:
            continue

        current_word, doc_id = data_mapped

        if old_word and old_word != current_word:
            print("{0} - {1} - {2}".format( old_word, total_count, doc_ids))
            doc_ids = []
            total_count = 0

        old_word = current_word
        doc_ids.append(doc_id)
        total_count += 1

    if old_word:
        print(old_word, '\t', total_count, '\t', ','.join(doc_ids))


# This function allows you to test the mapper with the provided test string
def main():
    reducer()

main()