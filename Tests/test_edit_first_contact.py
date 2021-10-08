from Model.contact import Contact


def test_add_contact(app):
    app.open_home_page()
    app.session.login(pwd="secret", login="admin")
    app.contact.edit_first(Contact(firstname="new1", lastname="new2", company="new3", mobile="89452525"))
    app.session.logout()



