'''
def test_del_first_contact1(app):
    app.open_home_page()
    app.session.login(pwd="secret", login="admin")
    app.contact.del_first1()
    app.session.logout()
'''


def test_del_first_contact2(app):
    app.open_home_page()
    app.session.login(pwd="secret", login="admin")
    app.contact.del_first2()
    app.session.logout()
