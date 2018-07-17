# -*- coding: utf-8 -*-
import functools

def log(obj):
    #通过判断obj类型决定带参还是无参
    if isinstance(obj, str):
        #当我们使用@log('execute')调用的时候，Python 能够发现这一层的封装，并把参数传递到装饰器的环境中
        def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                print('%s %s():' % (obj, fn.__name__))
                return fn(*args, **kw)
            return wrapper
        return decorator
    else:
        @functools.wraps(obj)
        def wrapper(*args, **kw):
            print('call %s():' % obj.__name__)
            return obj(*args, **kw)
        return wrapper
            
if __name__ == '__main__':
@log
def sayhi():
    print('Hi World!')
#sayhi = log(sayhi)
 
@log('execute')
def sayhello():
    print('Hello World!')
#sayhello = log('execute')(sayhello)
    
sayhi()
sayhello()