#import mysql.connector
#import pymysql.cursors
from Fixture.orm import ORMfixture
from Model.group import Group

db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", pwd="")

'''try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
        '''
try:
    list = db.get_contact_list()
    for item in list:
        print(item)
    print(len(list))
finally:
    pass #  db.destroy()
