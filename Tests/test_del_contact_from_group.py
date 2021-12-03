from Fixture.orm import ORMfixture
import random
from Fixture.contact import Contact
from Fixture.group import Group
import allure


def test_add_contact_to_group(app):
    db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", pwd="")
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_9"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(gname="test_9"))
    with allure.step('Given a contact and group lists'):
        groups = db.get_group_list()
        contacts = []
        group_for_edit = Group()
        for group in groups:
            contacts = db.get_contacts_in_group(group)
            if len(contacts) > 0:
                group_for_edit = group
                break
        if len(contacts) == 0:
            print('No one contact exists in groups')
            contacts = db.get_contact_list()
            contact = random.choice(contacts)
            contacts = contact
            group_for_edit = random.choice(groups)
            app.contact.put_contact_to_group(contact.id, group_for_edit.id)

        contact_for_edit = random.choice(contacts)
    with allure.step('When I delete a contact %s from the group %s' % (contact_for_edit, group_for_edit)):
        app.contact.delete_contact_from_group(group_for_edit.id, contact_for_edit.id)
    with allure.step('Then the contact list is added group'):
        assert not db.assertion(group_for_edit, contact_for_edit)

