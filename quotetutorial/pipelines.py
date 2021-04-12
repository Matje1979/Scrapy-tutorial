
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
import  mysql.connector
from itemadapter import ItemAdapter


class QuotetutorialPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        ##mysql
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'myquotes',
            auth_plugin='mysql_native_password'
            )
        self.curr = self.conn.cursor()
        ##sqlite3
        # self.conn = sqlite3.connect("myquotes.db")
        
        # self.curr = self.conn.cursor()
        

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""CREATE TABLE quotes_tb(
                        title text,
                        author text,
                        tag text
                        ) """)

    def process_item(self, item, spider):
        self.store_db(item)
        print ("Pipeline :" + item['title'][0])
        print ("***********Printing item tag: ", item['tag'])
        return item

    def store_db(self, item):
        ##mysql
        self.curr.execute("""INSERT INTO quotes_tb VALUES(%s, %s, %s)""",(
            item['title'][0],
            item['author'][0],
            ",".join(item['tag'])
        ))
        ##sqlite3
        # self.curr.execute("""INSERT INTO quotes_tb VALUES(?, ?, ?)""",(
        #     item['title'][0],
        #     item['author'][0],
        #     ",".join(item['tag'])
        # ))
        self.conn.commit()


