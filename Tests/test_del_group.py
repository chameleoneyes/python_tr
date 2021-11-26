from Model.group import Group


def test_del_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(gname="test_9"))
    old_groups = app.group.get_group_list()
    app.group.del_first()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups
