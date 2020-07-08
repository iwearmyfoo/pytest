# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    app.contact.edit_first(
        Contact("john2", "cena2", "osina", "vasya", "title", "company", "address", "6666", "7777", "8888",
                "9999", "a@a.com", "s@s.com", "d@d.com", "f.ru", "1", "January", "2000", "1", "January",
                "2010", "2", "g.ru", "tones"))
