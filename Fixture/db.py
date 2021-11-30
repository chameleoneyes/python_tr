import pymysql.cursors
from Model.group import Group
from Model.contact import Contact


class DBfixture:

    def __init__(self, host, name, user, pwd):
        self.host = host
        self.name = name
        self.user = user
        self.pwd = pwd
        self.connection = pymysql.connect(host=self.host, database=self.name, user=self.user, password=self.pwd,
                                          autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(gid=str(id), gname=name, gheader=header, gfooter=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()
