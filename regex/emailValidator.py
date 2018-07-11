import re
    
def is_valid_email(addr):
    re_email = re.compile(r'^([\w_.]+)@(\w+)\.(\w+)$')
    return re_email.match(addr)
    
def name_of_email(addr):
    re_email_with_name = re.compile(r'^(<[A-Z][a-z]+\s?[A-Z][a-z]+>){0,1}\s{0,1}([\w_.]+)@(\w+)\.(\w+)$')
    match = re_email_with_name.match(addr)
    if match:
        nametuple = match.groups()
        #含名字的地址
        if(nametuple[0]):
            #去除首尾两端的尖括号
            name = nametuple[0][1:][:-1]
        #不含名字的地址
        else:
            name = nametuple[1]
    else:
        name = ''
    return name