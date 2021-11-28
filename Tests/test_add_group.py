# -*- coding: utf-8 -*-

from Model.group import Group
import pytest
import random
import string
import re


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    s = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    s = s.strip()
    s = re.sub('\s+',' ', s)
    return prefix + s


tdata = [Group(gname="", gheader="", gfooter="")] + [
    Group(gname=random_string("name", 10), gheader=random_string("header", 5), gfooter=random_string("footer", 8))
    for i in range(5)
]


@pytest.mark.parametrize("group", tdata, ids=[repr(x) for x in tdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.gr_id_fill) == sorted(new_groups, key=Group.gr_id_fill)



