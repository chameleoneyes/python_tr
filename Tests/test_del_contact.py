# Delete contact from home page with Delete Button
def test_del_first_contact_hp(app):
    app.open_home_page()
    app.session.login(pwd="secret", login="admin")
    app.contact.del_first_from_home_page()
    app.session.logout()


# Delete contact from edit form
def test_del_first_contact_ef(app):
    app.open_home_page()
    app.session.login(pwd="secret", login="admin")
    app.contact.del_first_from_edit_form()
    app.session.logout()


# Delete all contacts from home page
def test_dell_all_contacts(app):
    app.open_home_page()
    app.session.login(pwd="secret", login="admin")
    app.contact.del_all()
    app.session.logout()
