def trim(s):
    if s != '':
        i = 0
        while s[i] == ' ':
            i = i + 1
            if i == len(s):
                s = ''
                break
        if s != '':
            j = -1
            while s[j] == ' ':
                j = j - 1
            if j == -1:
                s = s[i:]
            else:
                s = s[i:j + 1]    
    return s