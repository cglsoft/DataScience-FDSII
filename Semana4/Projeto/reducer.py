import sys

def reducer():
    oldKey = ""
    acc = 0

    try:
        for line in sys.stdin:
            key, value = line.strip().split("\t")
            
            if key != oldKey:
                if oldKey:
                    print("{0}\t{1}".format(oldKey, acc))
                acc = float(value)            
                oldKey = key
            else:
                acc += float(value)

        if oldKey:
            print("{0}\t{1}".format(oldKey, acc))
        

    except Exception as e:
        raise RuntimeError("Reason %s" % str(e))

data_Directory = "data"        
sys.stdin = open(data_Directory + '/mapper_result.txt')
sys.stdout = open(data_Directory + '/reducer_result.txt', 'w')

reducer()