def is_palindrome(n):
    if not isinstance(n, int):
        return False
    #先转为字符串
    s = str(n)
    #循环比较第n个字符和倒数第n个字符
    i = 0
    while i <= len(s) / 2:
        if s[i] != s[len(s) - 1 - i]:
            return False
        i += 1
    #若游标到达数字位数的一半，说明为回文数
    return True

#用[::-1]就能倒转字符串
def is_palindrome2(n):
    if not isinstance(n, int):
        return False
    s = str(n)
    return s == s[::-1]
    
if __name__ == '__main__':
    # 测试:
    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))
    if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
    else:
        print('测试失败!')