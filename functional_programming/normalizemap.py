def normalize(name):
    if isinstance(name, str):
        return name.capitalize()
    else:
        return ''
        
if __name__ == '__main__':
    # 测试:
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)