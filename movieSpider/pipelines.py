# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
from movieSpider.settings import table_name, mysql_port, mysql_db, mysql_passwd, mysql_user, mysql_host

HOST = 'localhost'
MYSQL_DBNAME = 'dev04'
MYSQL_PASSWORD = '123456'
MYSQL_USER = 'root'
MYSQL_PORT = '3306'

class MoviespiderPipeline(object):
    def __init__(self):
        # 连接数据库
        # self.conn=pymysql.connect(host=host,port=port,user=user,password=passwd,db=database,charset='utf8')
        self.conn = pymysql.connect(host=mysql_host, user=mysql_user, password=mysql_passwd, db=mysql_db,
                                    port=mysql_port)
        # 创建游标对象
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        # 将item转化为dict类型
        data = dict(item)
        # 将数据插入数据库
        self.cur.execute(
            "INSERT INTO movie_top250 (serial_number,film_name,film_country,film_time,film_type,film_maker,film_score,film_quote) VALUE (%(serial_number)s,%(film_name)s,%(film_country)s,%(film_time)s,%(film_type)s,%(film_maker)s,%(film_score)s,%(film_quote)s)",
            data)
        self.conn.commit()
        return item

