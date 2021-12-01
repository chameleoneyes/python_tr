from Model.contact import Contact
import time
import random



# Delete contact from home page with Delete Button
def test_del_random_contact_hp(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_9"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id_from_hp(contact.id)
    time.sleep(2)       # for 1 assert
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.con_id_fill) == \
               sorted(app.contact.get_contact_list(), key=Contact.con_id_fill)



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
