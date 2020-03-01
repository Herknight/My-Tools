"""
ｄｉｃｔ 所有数据库交互
提供数据库连接，以及功能交互
"""
import pymysql
import hashlib

salt = b"*#06#"  # 加密专用盐


# 　加密处理函数
def encryption(passwd):
    # 对密码进行加密处理
    hash = hashlib.md5(salt)
    hash.update(passwd.encode())
    return hash.hexdigest()  # 获取存储密码


class Database:
    def __init__(self):
        # 连接数据库
        self.db = pymysql.connect(host='localhost',
                                  port=3306,
                                  user='root',
                                  password='123456',
                                  database='dict',
                                  charset='utf8')

        # 创建游标 (操作数据库语句,获取查询结果)
        self.cur = self.db.cursor()

    def close(self):
        # 关闭游标和数据库
        self.cur.close()
        self.db.close()

    def register(self, name, passwd):
        # 判断用户名
        sql = "select * from user where name='%s'" % name
        self.cur.execute(sql)
        resule = self.cur.fetchone()
        if resule:
            return False

        # 　加密
        passwd = encryption(passwd)

        # 插入用户
        try:
            sql = "insert into user (name,passwd) values (%s,%s)"
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def login(self, name, passwd):
        passwd = encryption(passwd)  # 加密转换

        sql = "select * from user where name='%s' and passwd='%s'" % (name, passwd)
        self.cur.execute(sql)
        result = self.cur.fetchone()
        if result:
            return True
        else:
            return False

    def query(self, word):
        sql = "select mean from words where word='%s'" % word
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return r[0]

    # 　插入记录
    def insert_history(self, name, word):
        sql = "insert into hist (name,word) \
        values (%s,%s)"
        try:
            self.cur.execute(sql, [name, word])
            self.db.commit()
        except:
            self.db.rollback()

    def history(self,name):
        sql = "select name,word,time from hist \
        where name='%s' order by time desc " \
              "limit 10"%name
        self.cur.execute(sql)
        return self.cur.fetchall()