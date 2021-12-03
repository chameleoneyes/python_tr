from Model.group import Group
import random
import allure


def test_edit_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(gname="test_9"))
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    oldgroup = random.choice(old_groups)
    with allure.step('When I add a group %s to the list' % oldgroup):
        newgroup = oldgroup
        newgroup.gname = "1new1"
        app.group.edit_group_by_id(newgroup, oldgroup.id)
#    assert len(old_groups) == app.group.count()
    with allure.step('Then the new group list is equal to the old group list with edited group'):
        new_groups = db.get_group_list()
        index = old_groups.index(oldgroup)
        old_groups[index] = newgroup
    #    assert sorted(old_groups, key=Group.gr_id_fill) == sorted(new_groups, key=Group.gr_id_fill)
        assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.gr_id_fill) == sorted(app.group.get_group_list(), key=Group.gr_id_fill)


#def test_edit_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(gname="test_9"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first(Group(gheader="1new2"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_edit_group(app):
#    if app.group.count() == 0:
#        app.group.create(Group(gname="test_9"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first(Group(gname="new1", gheader="new2", gfooter="new3"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
