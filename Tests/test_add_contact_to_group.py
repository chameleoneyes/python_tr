from Fixture.orm import ORMfixture
import random
from Fixture.contact import Contact
from Fixture.group import Group
from Fixture.orm import ORMfixture
import allure

def test_add_contact_to_group(app):
    db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", pwd="")
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_9"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(gname="test_9"))
    with allure.step('Given a contact and group lists'):
        groups = db.get_group_list()
        contacts = db.get_contact_list()
        contact_for_edit = random.choice(contacts)
        group_for_edit = random.choice(groups)
    with allure.step('When I add a contact %s to the group %s' % (contact_for_edit, group_for_edit)):
        app.contact.put_contact_to_group(contact_for_edit.id, group_for_edit.id)
    with allure.step('Then the contact list is added group'):
        assert db.assertion(group_for_edit, contact_for_edit)




