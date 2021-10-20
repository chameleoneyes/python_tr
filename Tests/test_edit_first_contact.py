from Model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_9"))
    app.contact.edit_first(Contact(firstname="new1", lastname="new2", mobile="89452525"))

