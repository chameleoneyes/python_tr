from Model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_9"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="new1", lastname="new2", addr="89452525")
    app.contact.edit_first(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.con_id_fill) == sorted(new_contacts, key=Contact.con_id_fill)


