

def test_del_first_group(app):
    app.open_home_page()
    app.session.login(pwd="secret", login="admin")
    app.group.del_first1()
    app.session.logout()
