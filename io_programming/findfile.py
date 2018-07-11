import os, re

def findfile(str):
    #首先查找当前目录
    currentlist = [x for x in os.listdir('.') if os.path.isfile(x) and re.match(str, x)]
    for n in currentlist:
        print(os.path.join('.', n))
    #找到所有子目录
    subdirlist = [y for y in os.listdir('.') if os.path.isdir(y)]
    #对所有子目录查找文件
    for path in subdirlist:
        subfilelist = [z for z in os.listdir(os.path.join('.', path)) if os.path.isfile(os.path.join('.', path, z)) and re.match(str, z)]
        for p in subfilelist:
            print(os.path.join('.', path, p))