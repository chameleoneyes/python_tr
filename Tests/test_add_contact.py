# -*- coding: utf-8 -*-

import pytest
from Model.contact import Contact
from Fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.clear_fixture)
    return fixture


def test_add_contact(app):
    app.open_home_page()
    app.session.login(pwd="secret", login="admin")
    app.contact.add_contact(Contact(firstname="test1", lastname="test2", company="test3", mobile="89456464564"))
    app.session.logout()


