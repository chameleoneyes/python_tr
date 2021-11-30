# -*- coding: utf-8 -*-

from Model.group import Group
import pytest
from data.groups import tdata


# @pytest.mark.parametrize("group", tdata, ids=[repr(x) for x in tdata])


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.gr_id_fill) == sorted(new_groups, key=Group.gr_id_fill)
    if check_ui:
        assert sorted(new_groups, key=Group.gr_id_fill) == sorted(app.group.get_group_list(), key=Group.gr_id_fill)



