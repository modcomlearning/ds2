
filename = 'sample.txt'
with open(filename) as fn:
    # Read each line
    ln = fn.readline()
    # Keep count of lines
    lncnt = 1
    while ln:
        print("Line {}: {}".format(lncnt, ln.strip()))
        ln = fn.readline()
        lncnt += 1




from collections import Counter
with open(r'sample.txt') as f:
    p = Counter(f.read().split())
    print(p)

import pandas
df = pandas.DataFrame.from_dict(p, orient='index').reset_index()
print(df['index'])







