# -*- coding: gbk -*-
#   生成若干个16位激活码，并保存到MySQL与Redis数据库中
#   第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
#   第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
#   第 0003 题： 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。

import random
import pymysql
import redis

list = []
key_list = []
list_len = 1000
r = redis.Redis(host = '127.0.0.1', port = 6379, db = 0)  #连接到redis

class KEY(object):
    def __init__(self):     #大小写字母、数字
        for x in range(65, 91):
            list.append(str(chr(x)))

        for x in range(97, 123):
            list.append(str(chr(x)))

        for x in range(10):
            list.append(str(x))

    def get_key(self):      #随机生成激活码
        s = ''
        for x in range(16):
            a = random.choice(list)
            s = s + a
        return s

class MySQL_op():
    def __init__(self):     #连接到MySQL
        #这里是事先建好的用户guest和数据库product_key
        self.conn = pymysql.connect(host='127.0.0.1', port=3306,
                               user='guest', password='Guest.618',
                               database='product_key', charset='utf8mb4')

    def mysql_commit(self):
        for i in range(list_len):
            try:
                with self.conn.cursor() as cursor:      #将激活码插入数据库，这里使用ignore方式跳过重复的激活码
                    affected_rows = cursor.execute(
                        'insert ignore into `keys` values (%s, %s)',
                        (i, key_list[i])
                    )
                if affected_rows == 1:
                    print('Insert product key: %s. Finished.' % key_list[i])
                self.conn.commit()  #提交事务
            except pymysql.MySQLError as err:
                self.conn.rollback()    #回滚事务
                print(type(err), err)
        self.conn.close()

if __name__ == '__main__':
    key = KEY()
    dup_keys = 0
    print('Product keys:')
    for x in range(list_len):
        product_key = key.get_key()
        while product_key in key_list:      #去除重复的激活码
            product_key = key.get_key()
            dup_keys += 1
        print(product_key)
        key_list.append(product_key)
    print(len(key_list), 'keys generated.')
    print(dup_keys, 'duplicated keys appeared.')

    sqlop = MySQL_op()  #存入MySQL
    sqlop.mysql_commit()

    for i in range(list_len):   #存入Redis
        r.set(i, key_list[i])
