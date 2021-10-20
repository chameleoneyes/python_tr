from Model.contact import Contact


# Delete contact from home page with Delete Button
def test_del_first_contact_hp(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_9"))
    app.contact.del_first_from_home_page()


# Delete contact from edit form
def test_del_first_contact_ef(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_9"))
    app.contact.del_first_from_edit_form()


# Delete all contacts from home page
def test_dell_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_9"))
    app.contact.del_all()
