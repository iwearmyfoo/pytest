from model.group import Group


def test_delete_contact(app):
    app.contact.delete_first()
