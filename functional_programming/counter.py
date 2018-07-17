def createCounter():
    s = 0
    def counter():
        nonlocal s
        s += 1
        return s
    return counter
    
def createCounter2():
    def _integer_iter():
        n = 0
        while True:
            n += 1
            yield n
    iter = _integer_iter()
    def counter():
        return next(iter)
    return counter