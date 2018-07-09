#hand-grenade sort, a near-enough is good enough implementation of quicksort
import random
randlist = []

for x in range(10):
	randlist.append(random.randint(1,51))

def hgSort(list):
	l = []
	e = []
	g = []
	hg = []
	out = []

	if len(list) >1:
		pivot = list[0]
		for x in list:
			if x < pivot and random.randint(0,101) < 95:
				l.append(x)
			if x == pivot:
				e.append(x)
			if x > pivot and random.randint(0,101) < 95:
				g.append(x)
			else: hg.append(x)
		out = hgSort(l)+e+hgSort(g)

		for x in hg:
			out.insert(random.randint(0,len(out)),x)
		print out
	else:
		return list
