# hand-grenade sort, a near-enough is good enough implementation of quicksort
import random

randlist = []

for x in range(10):
    randlist.append(random.randint(1, 51))


def hgSort(inlist):
    l = []
    e = []
    g = []
    hg = []

    if len(inlist) > 1:
        pivot = inlist[0]
        for x in inlist:
            if x < pivot and random.randint(0, 101) < 95:
                l.append(x)
            if x == pivot:
                e.append(x)
            if x > pivot and random.randint(0, 101) < 95:
                g.append(x)
            elif len(hg) > 0:
                hg.append(x)
        out = hgSort(l) + e + hgSort(g)

        for x in hg:
            out.insert(random.randint(0, len(out)), x)
        return out
    else:
        return inlist


print hgSort(randlist)
