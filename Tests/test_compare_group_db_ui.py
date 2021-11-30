from Model.group import Group


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
            return Group(gid=group.id, gname=group.gname.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.gr_id_fill) == sorted(db_list, key=Group.gr_id_fill)
