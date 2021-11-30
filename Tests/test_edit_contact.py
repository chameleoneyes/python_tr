from Model.contact import Contact
import random


def test_edit_random_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_9"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    contact.firstname = "new1"
    contact.lastname = "new2"
    contact.addr = "89452525"
    app.contact.edit_contact_by_id(contact, contact.id)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.con_id_fill) == sorted(new_contacts, key=Contact.con_id_fill)
    if check_ui:
        assert sorted(new_contacts, key=Contact.con_id_fill) == \
               sorted(app.contact.get_contact_list(), key=Contact.con_id_fill)


