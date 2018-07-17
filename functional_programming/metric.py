# -*- coding: utf-8 -*-
import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        #获取当前时间用time.time()
        begintime = time.time()
        func = fn(*args, **kw)
        endtime = time.time()
        #endtime减去begintime得到fn执行时间
        print('%s executed in %s ms' % (fn.__name__, endtime - begintime))
        return func
    return wrapper