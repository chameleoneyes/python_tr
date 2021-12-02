from pony.orm import *
from datetime import datetime
from Model.group import Group
from Model.contact import Contact


class ORMfixture:

    db = Database()

    class ORMgroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMfixture.ORMcontact, table='address_in_groups', column='id', reverse='groups', lazy=True)

    class ORMcontact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        addr = Optional(str, column='address')
        homephone = Optional(str, column='home')
        mobile = Optional(str, column='mobile')
        workphone = Optional(str, column='work')
        phone2 = Optional(str, column='phone2')
        email1 = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        groups = Set(lambda: ORMfixture.ORMgroup, table='address_in_groups', column='group_id', reverse='contacts', lazy=True)

    def __init__(self, host, name, user, pwd):
        self.db.bind('mysql', host=host, database=name, user=user, password=pwd)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups(self, groups):
        def convert(group):
            return Group(gid=str(group.id), gname=group.name, gheader=group.header, gfooter=group.footer)
        return list(map(convert, groups))

    def convert_contacts(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname, addr=contact.addr,
                           homephone=contact.homephone, mobile=contact.mobile, workphone=contact.workphone, phone2=contact.phone2,
                           email1=contact.email1, email2=contact.email2, email3=contact.email3)
        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
       # with db_session:
        return self.convert_groups(select(gr for gr in ORMfixture.ORMgroup))

    @db_session
    def get_contact_list(self):
        # with db_session:
        return self.convert_contacts(select(con for con in ORMfixture.ORMcontact if con.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(gr for gr in ORMfixture.ORMgroup if gr.id == group.id))[0]
        return self.convert_contacts(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(gr for gr in ORMfixture.ORMgroup if gr.id == group.id))[0]
        return self.convert_contacts(
            select(con for con in ORMfixture.ORMcontact if con.deprecated is None and orm_group not in con.groups))

    @db_session
    def get_group_contains_contact(self, contact):
        orm_contact = list(select(con for con in ORMfixture.ORMcontact if con.deprecated is None and con.id == contact.id))
        return self.convert_groups(
            select(gr for gr in ORMfixture.ORMgroup if orm_contact in gr.contacts))

    @db_session
    def get_contact_deleted_from_group(self, group):
        contact = Contact()
        contact.id = (self.db.execute
                        ("select id from address_in_groups where group_id=%s and deprecated is NULL" % group.id))
        return contact

    def assertion(self, group, contact_for_edit):
        contacts_in_group = self.get_contacts_in_group(group)
        i = False
        for contact in contacts_in_group:
            if contact == contact_for_edit:
                i = True
        return i
