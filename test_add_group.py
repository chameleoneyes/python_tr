# -*- coding: utf-8 -*-

import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.clear_fixture)
    return fixture


def test_add_group(app):
    app.open_home_page()
    app.login(pwd="secret", login="admin")
    app.create_group(Group(gname="test", gheader="test2", gfooter="test3"))
    app.logout()
