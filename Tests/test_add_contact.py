# -*- coding: utf-8 -*-

from Model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="test1", lastname="test2", addr="test3")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.con_id_fill) == sorted(new_contacts, key=Contact.con_id_fill)




#    app.contact.create(Contact(firstname="test1", lastname="test2", company="test3", mobile="9456464564"))
#    app.contact.create(Contact(firstname="test2", lastname="test2", company="test3", mobile="9456464564"))
#    app.contact.create(Contact(firstname="test3", lastname="test2", company="test3", mobile="9456464564"))
#    app.contact.create(Contact(firstname="test4", lastname="test2", company="test3", mobile="9456464564"))
#    app.contact.create(Contact(firstname="test5", lastname="test2", company="test3", mobile="9456464564"))


