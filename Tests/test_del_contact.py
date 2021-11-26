from Model.contact import Contact
import time
from random import randrange


# Delete contact from home page with Delete Button
def test_del_random_contact_hp(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_9"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts)) - 1
    app.contact.del_random_from_home_page(index)
    time.sleep(2)       # for 1 assert
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts



# Delete contact from edit form
#def test_del_first_contact_ef(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test_9"))
#    app.contact.del_first_from_edit_form()


# Delete all contacts from home page
#def test_dell_all_contacts(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test_9"))
#    app.contact.del_all()
