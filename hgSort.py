# hand-grenade sort, a near-enough is good enough implementation of quicksort
import random

randlist = []

for x in range(10):
    randlist.append(random.randint(1, 20))


def hgSort(inlist):
    l = []
    e = []
    g = []
    hg = []
    scannedOnce = False

    if len(inlist) > 1:
        pivot = inlist[0]
        for x in inlist:
            if x < pivot and scannedOnce is False and random.randint(0, 101) < 95:
                l.append(x)
            elif scannedOnce is True:
                    l.append(x)
            if x == pivot:
                e.append(x)
            if x > pivot and scannedOnce is False and random.randint(0, 101) < 95:
                g.append(x)
            elif scannedOnce is True:
                    g.append(x)
            else:
                hg.append(x)
        scannedOnce = True
        out = hgSort(l) + e + hgSort(g)

        for y in hg:
            out.insert(random.randint(0, len(out)), y)
        return out
    else:
        return inlist


print randlist
print hgSort(randlist)
