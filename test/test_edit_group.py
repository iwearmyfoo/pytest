from model.group import Group


def test_edit_first(app):
    app.group.edit_first(Group(name="nameNew", header="headNew", footer="footNew"))


def test_edit_name(app):
    app.group.edit_first(Group(name="nameNew"))
