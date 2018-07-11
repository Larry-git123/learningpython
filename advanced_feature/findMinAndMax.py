def findMinAndMax(L):
    if len(L) == 0:
        min = None
        max = None
    else:
        min = L[0]
        max = L[0]
        for n in L:
            if n > max:
                max = n
            if n < min:
                min = n
    return min, max