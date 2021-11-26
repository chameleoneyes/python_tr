from Model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_9"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="new1", lastname="new2", addr="89452525")
    app.contact.edit_first(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts) == sorted(new_contacts)


