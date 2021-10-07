# -*- coding: utf-8 -*-

from Model.group import Group


def test_add_group(app):
    app.open_home_page()
    app.session.login(pwd="secret", login="admin")
    app.group.create(Group(gname="test", gheader="test2", gfooter="test3"))
    app.session.logout()
