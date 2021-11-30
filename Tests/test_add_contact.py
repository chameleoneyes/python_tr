# -*- coding: utf-8 -*-

from Model.contact import Contact


def test_add_contact(app, json_contacts, db, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.con_id_fill) == sorted(new_contacts, key=Contact.con_id_fill)
    if check_ui:
        assert sorted(new_contacts, key=Contact.con_id_fill) == \
               sorted(app.contact.get_contact_list(), key=Contact.con_id_fill)

