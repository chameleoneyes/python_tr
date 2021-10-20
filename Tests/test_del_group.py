from Model.group import Group


def test_del_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(gname="test_9"))
    app.group.del_first()
