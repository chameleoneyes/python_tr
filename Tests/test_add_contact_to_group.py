from Model.contact import Contact
from Fixture.orm import ORMfixture
import random
from Fixture.contact import Contact


def test_add_contact_to_group(app):
    db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", pwd="")
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_9"))
    groups = db.get_group_list()
    contacts = db.get_contact_list()

    '''    contacts_not_in_groups = []
    contacts_in_group = []
    for group in groups:
        contacts_in_group.append(db.get_contacts_in_group(group))
    for contact in contacts:
        if contact not in contacts_in_group:
            contacts_not_in_groups.append(contact)
            '''

    contact_for_edit = random.choice(contacts)
    group_for_edit = random.choice(groups)
    app.contact.put_contact_to_group(contact_for_edit.id, group_for_edit.id)
    contacts_in_group = db.get_contacts_in_group(group_for_edit)

    def assertion():
        i = False
        for contact in contacts_in_group:
            if contact == contact_for_edit:
                i = True
        return i

    assert assertion()


