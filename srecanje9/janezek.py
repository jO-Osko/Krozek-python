from functools import lru_cache

kovanci = [2, 4, 1, 3, 4] *100
dolzina = len(kovanci)

@lru_cache(maxsize=None)
def najvec_kovancev(index_zacetka):

    ostanek = dolzina - index_zacetka
    if ostanek == 1:
        return kovanci[index_zacetka]
    elif ostanek == 2:
        return max(kovanci[-1], kovanci[-2])
    
    # Izberemo ali ne izberemo kovanca na index_zacetka
    # 1. izberemo
    izberemo = kovanci[index_zacetka] + \
        najvec_kovancev(index_zacetka + 2)
    
    ne_izberemo = najvec_kovancev(index_zacetka + 1)

    return max(izberemo, ne_izberemo)

import time
t = time.time()
print(najvec_kovancev(0))
print(time.time() - t)

while len(a) != 0:
    # 
    pass
    a = []