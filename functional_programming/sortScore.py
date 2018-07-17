def by_name(t):
    if not isinstance(t, tuple):
        raise TypeError
    return t[0].capitalize()
    
def by_score(t):
    if not isinstance(t, tuple):
        raise TypeError
    return float(t[1])
    
if __name__ == '__main__':
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    L2 = sorted(L, key=by_name)
    print(L2)