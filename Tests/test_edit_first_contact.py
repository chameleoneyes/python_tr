from Model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first(Contact(firstname="new1", lastname="new2", mobile="89452525"))

