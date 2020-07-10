from model.group import Group


def test_edit_first(app):
    if app.group.count() == 0:
        app.group.create(Group(name="edit"))
    app.group.edit_first(Group(name="nameNew", header="headNew", footer="footNew"))


def test_edit_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="edit"))
    app.group.edit_first(Group(name="nameNew"))
