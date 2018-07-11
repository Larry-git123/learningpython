def yh_triangles():
    old_list = [1]
    while True:
        yield old_list
        new_list = [1]
        n = 0
        while n < len(old_list):
            new_list.append(sum(old_list[n:n+2]))
            n += 1
        old_list = new_list