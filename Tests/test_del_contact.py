from Model.contact import Contact
import time


# Delete contact from home page with Delete Button
def test_del_first_contact_hp(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_9"))
    old_contacts = app.contact.get_contact_list()
    for i in range(len(old_contacts)):
        print(str(old_contacts[i].id) + " : " + str(old_contacts[i].firstname))
    print("New contacts")

    app.contact.del_first_from_home_page()
    time.sleep(2)       # for 1 assert
    new_contacts = app.contact.get_contact_list()
    for i in range(len(new_contacts)):
        print(str(new_contacts[i].id) + " : " + str(new_contacts[i].firstname))
    assert len(old_contacts) - 1 == len(new_contacts)



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
