import random
from Model.group import Group


def test_del_random_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(gname="test_9"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.del_group_by_id(group.id)
#    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.gr_id_fill) == sorted(app.group.get_group_list(), key=Group.gr_id_fill)
