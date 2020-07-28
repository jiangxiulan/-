import pymysql
import traceback
from time import sleep

################################################################################
#数据库操作


class PyMySQL(object):
    def __init__(self,order):
        self.host='localhost'
        self.user='ruangong'
        self.pwd='123456'
        self.db='shopping'
        self.order=order
        self.conn = pymysql.connect(self.host, self.user, self.pwd, self.db)
        self.cursor = self.conn.cursor()

    def create_table_func(self):
        self.cursor.execute(self.order)
        print('数据表创建完毕')

    def insert_date(self):
        try:
            self.cursor.execute(self.order)
            self.conn.commit()
            return 0
        except:
            print(traceback.format_exc())
            self.conn.rollback()
            return 1

    def update_data(self):
        try:
            self.cursor.execute(self.order)
            self.conn.commit()
        except:
            print(traceback.format_exc())
            self.conn.rollback()

    def delete_data(self):
        try:
            self.cursor.execute(self.order)
            self.conn.commit()
        except:
            print(traceback.format_exc())
            self.conn.rollback()

    def select_data(self,total):
        self.cursor.execute(self.order)

        all_data = self.cursor.fetchall()
        for i in all_data:
            total=i[0]
        return  total

    def select_data2(self,list):
        self.cursor.execute(self.order)

        all_data = self.cursor.fetchall()
        # print(all_data)
        # print(len(list))
        # print(len(all_data))
        # print(min(len(list),len(all_data)))
        for i in range(0,min(len(list),len(all_data))):
            list[i]=''
            list[i]=all_data[i]
        # print(list)
        return  list

