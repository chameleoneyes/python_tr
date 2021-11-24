from Model.group import Group


#def test_edit_group_name(app):
#    if app.group.count() == 0:
#        app.group.create(Group(gname="test_9"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first(Group(gname="1new1"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_edit_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(gname="test_9"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first(Group(gheader="1new2"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(gname="test_9"))
    old_groups = app.group.get_group_list()
    app.group.edit_first(Group(gname="new1", gheader="new2", gfooter="new3"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
