# Delete contact from home page with Delete Button
def test_del_first_contact_hp(app):
    app.contact.del_first_from_home_page()


# Delete contact from edit form
def test_del_first_contact_ef(app):
    app.contact.del_first_from_edit_form()


# Delete all contacts from home page
def test_dell_all_contacts(app):
    app.contact.del_all()
