from Model.group import Group


def test_edit_group_name(app):
    app.group.edit_first(Group(gname="1new1"))


def test_edit_group_header(app):
    app.group.edit_first(Group(gheader="1new2"))


def test_edit_group(app):
    app.group.edit_first(Group(gname="new1", gheader="new2", gfooter="new3"))
