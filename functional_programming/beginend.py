# -*- coding: utf-8 -*-
import functools

def beginend(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('begin call')
        func = fn(*args, **kw)
        print('end call')
        return func
    return wrapper