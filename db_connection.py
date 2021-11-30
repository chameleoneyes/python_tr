#import mysql.connector
#import pymysql.cursors
from Fixture.db import DBfixture

db = DBfixture(host="127.0.0.1", name="addressbook", user="root", password="")

'''try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
        '''
try:
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))
finally:
    db.destroy()
