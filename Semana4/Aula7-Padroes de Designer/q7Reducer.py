#!/usr/bin/python

import sys

def reducer():

    old_word = None
    doc_ids = []
    total_count = 0

    try:
        for line in sys.stdin:
            data_mapped = line.strip().split("\t")
            
            if len(data_mapped) != 2:
                continue

            current_word, doc_id = data_mapped

            if old_word and old_word != current_word:
                print old_word, '\t', total_count, '\t', ','.join(doc_ids)
                doc_ids = []
                total_count = 0

            old_word = current_word
            doc_ids.append(doc_id)
            total_count += 1

        if old_word:
            print(old_word, '\t', total_count, '\t', ','.join(doc_ids))

    except Exception as e:
        raise RuntimeError("Error %s" % str(e))


def main():
    reducer()

main()