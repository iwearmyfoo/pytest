# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from contact import Contact
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_contact(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")
        self.login(wd, login="admin", password="secret")
        self.add_contact(wd, Contact("john", "cena", "osina", "vasya", "title", "company", "address", "6666", "7777", "8888",
                         "9999", "a@a.com", "s@s.com", "d@d.com", "f.ru", "1", "January", "2000", "1", "January",
                         "2010", "2", "g.ru", "tones"))
        self.logout(wd)

    def add_contact(self, wd, contact):
        # open contact page
        wd.find_element_by_link_text("add new").click()
        # fill contact page
        wd.find_element_by_name("firstname").send_keys(contact.fistname)
        wd.find_element_by_name("middlename").send_keys(contact.midname)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.homephone)
        wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
        wd.find_element_by_name("work").send_keys(contact.workphone)
        wd.find_element_by_name("fax").send_keys(contact.faxphone)
        wd.find_element_by_name("email").send_keys(contact.firstmail)
        wd.find_element_by_name("email2").send_keys(contact.secondmail)
        wd.find_element_by_name("email3").send_keys(contact.thirdmail)
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("address2").send_keys(contact.secondaryaddress)
        wd.find_element_by_name("phone2").send_keys(contact.additionalphone)
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # apply contact data
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def login(self, wd, login, password):

        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

        def tearDown(self):
            self.wd.quit()
            self.assertEqual([], self.verificationErrors)

