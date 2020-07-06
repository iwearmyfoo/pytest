from model.group import Group


def test_edit_first(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="nameNew", header="headNew", footer="footNew"))
    app.session.logout()
