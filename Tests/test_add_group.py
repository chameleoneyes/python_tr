# -*- coding: utf-8 -*-

from Model.group import Group
import pytest
import allure
from data.groups import tdata


# @pytest.mark.parametrize("group", tdata, ids=[repr(x) for x in tdata])


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step('When I add a group %s to the list' % group):
        app.group.create(group)
    with allure.step('Then the new group list is equal to the old group list with added new group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.gr_id_fill) == sorted(new_groups, key=Group.gr_id_fill)
#    if check_ui:
#        assert sorted(new_groups, key=Group.gr_id_fill) == sorted(app.group.get_group_list(), key=Group.gr_id_fill)



