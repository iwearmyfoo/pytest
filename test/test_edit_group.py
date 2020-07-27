from model.group import Group


def test_edit_first(app):
    if app.group.count() == 0:
        app.group.create(Group(name="edit"))
    app.group.edit_first(Group(name="nameNew", header="headNew", footer="footNew"))


def test_edit_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="nameNew")
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.create(Group(name="edit"))
    app.group.edit_first(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
