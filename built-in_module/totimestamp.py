import re
from datetime import datetime, timedelta, timezone

def to_timestamp(dt_str, tz_str):
    re_dt = re.compile(r'^(\d+)\-(0[0-9]|1[0-2]|[0-9])\-(0[0-9]|1[1-9]|2[0-9]|3[0-1]|[0-9])\s(0[0-9]|1[1-9]|2[0-3]):([0-5][0-9]|[0-9]):([0-5][0-9]|[0-9])$')
    re_tz = re.compile(r'^(UTC|utc)(\+|\-)(0[0-9]|1[0-2]|[0-9])(:00)?$')
    #校验时间输入
    dt_match = re_dt.match(dt_str)
    if dt_match:
        #生成datetime
        dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
        #校验时区输入
        tz_match = re_tz.match(tz_str)
        if tz_match:
            #获得时区信息
            tz_tuple = tz_match.groups()
            orphan = tz_tuple[1]
            if orphan == '+':
                delta = int(tz_tuple[2])
            elif orphan == '-':
                delta = -1 * int(tz_tuple[2])
            tz = timezone(timedelta(hours=delta))
            #设置时区
            dt = dt.replace(tzinfo=tz)
            #转换为timestamp
            ts = dt.timestamp()
        else:
            #时区输入错误
            ts = -2.0  
    else:
        #时间输入错误
        ts = -1.0
    return ts