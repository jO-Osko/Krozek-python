# 0  1  1  2  3  5  8  13 ...
# a  b->c
#    a  b->c

max_velikost = 10**6

predzadnji = 0
zadnji = 1
while zadnji < max_velikost:
    naslednji = zadnji + predzadnji

    predzadnji = zadnji
    zadnji = naslednji

    print(naslednji)
