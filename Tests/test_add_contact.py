# -*- coding: utf-8 -*-

from Model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="test1", lastname="test2", company="test3", mobile="9456464564"))


