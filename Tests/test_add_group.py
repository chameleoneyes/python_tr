# -*- coding: utf-8 -*-

from Model.group import Group
from sys import maxsize


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(gname="test", gheader="test2", gfooter="test3")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)

    def gr_id_fill(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize
    assert sorted(old_groups, key=gr_id_fill) == sorted(new_groups, key=gr_id_fill)


#def test_add_empty_group(app):
#    app.group.create(Group(gname="", gheader="", gfooter=""))
