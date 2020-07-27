from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.add(Contact("john", "cena", "osina", "vasya", "title", "company", "address", "6666", "7777", "8888",
                            "9999", "a@a.com", "s@s.com", "d@d.com", "f.ru", "1", "January", "2000", "1", "January",
                            "2010", "2", "g.ru", "tones"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
