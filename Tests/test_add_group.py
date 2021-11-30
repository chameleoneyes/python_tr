# -*- coding: utf-8 -*-

from Model.group import Group
import pytest
from data.groups import tdata


# @pytest.mark.parametrize("group", tdata, ids=[repr(x) for x in tdata])


def test_add_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.gr_id_fill) == sorted(new_groups, key=Group.gr_id_fill)



