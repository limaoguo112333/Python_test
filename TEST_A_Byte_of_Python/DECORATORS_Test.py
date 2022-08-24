# -*- coding: gbk -*-
#一个关于装饰器的例题

from time import sleep
from functools import wraps
import logging
logging.basicConfig()
log = logging.getLogger("retry")

def retry(f):
    @wraps(f)
    def wrapped_f(*args, **kwargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1, MAX_ATTEMPTS + 1):  #尝试循环5次
            try:                #尝试执行save_to_database函数
                return f(*args, **kwargs)
            except:
                log.exception("Attempt %s/%s failed : %s",  #输出错误日志
                              attempt,
                              MAX_ATTEMPTS,
                              (args, kwargs))
                sleep(10 * attempt)
        log.critical("All %s attempts failed : %s",
                     MAX_ATTEMPTS,
                     (args, kwargs))
    return wrapped_f
counter = 0

@retry  #装饰器
def save_to_database(arg):
    print("Write to a database or make a network call or etc.")
    print("This will be automatically retried if exception is thrown.")
    global counter
    counter += 1
    if counter < 2:
        raise ValueError(arg)

if __name__ == '__main__':
    save_to_database("Some bad value")
