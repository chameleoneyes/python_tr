from Model.group import Group


def test_add_group(app):
    app.open_home_page()
    app.session.login(pwd="secret", login="admin")
    app.group.edit_first_group(Group(gname="new1", gheader="new2", gfooter="new3"))
    app.session.logout()
