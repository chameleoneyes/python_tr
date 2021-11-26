from Model.contact import Contact
from random import randrange


def test_edit_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_9"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="new1", lastname="new2", addr="89452525")
    index = randrange(len(old_contacts) - 1)
    contact.id = old_contacts[index].id
    app.contact.edit_random(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.con_id_fill) == sorted(new_contacts, key=Contact.con_id_fill)


