# -*- coding: utf-8 -*-

from Model.group import Group


def test_add_group(app):
    app.group.create(Group(gname="test", gheader="test2", gfooter="test3"))


def test_add_empty_group(app):
    app.group.create(Group(gname="", gheader="", gfooter=""))