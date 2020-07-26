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
        except:
            print(traceback.format_exc())
            self.conn.rollback()

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

    def select_data(self,str):
        self.cursor.execute(self.order)

        all_data = self.cursor.fetchall()
        for i in all_data:
            print('查询结果为：{}'.format(i))
            print(type(i[1]))
            str=i[1]
        return  str

    def select_data2(self,list):
        self.cursor.execute(self.order)

        all_data = self.cursor.fetchall()
        j=0
        for i in all_data:
            print('查询结果为：{}'.format(i))
            print(type(i[0]))
            list.insert(j,i)
            j=j+1
            print(list)

        return  list
#
# if __name__ == '__main__':
#     create_table = 'create table stu(id int not null primary key auto_increment,name varchar(255) not null,age int, sex varchar(255))default charset=utf8'
#     select = 'select * from user_inf'
#     update = 'update stu set name="明明" where id=2'
#     delete = 'delete from stu where id=9'
#     insert = 'insert into stu(name,age,sex) values("%s","%d","%s")' % ('小明', 2, "男")
#     order=select
#     my = PyMySQL(order)
#     #my.create_table_func()
#     #my.insert_date()
#     #my.update_data()
#     #my.delete_data()
#     my.select_data()
