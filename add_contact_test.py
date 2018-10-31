# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class AddContactTest(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username= "admin", password= "secret")
        self.add_contact(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def add_contact(self, wd):
        # init creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(u"Петр")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(u"Петрович")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(u"Петров")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(u"Директор")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(u"ООО Хороший софт")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(u"г. Город, ул. Улица, д. 1, оф. 305")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("1234567")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("2345678")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("3456789")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("4567890")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("email@goodsoft.ru")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("pr@goodsoft.ru")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("sales@goodsoft.ru")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("www.goodsoft.ru")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        wd.find_element_by_xpath("//option[@value='1']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("January")
        wd.find_element_by_xpath("//option[@value='January']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1970")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("2")
        wd.find_element_by_xpath("(//option[@value='2'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("April")
        wd.find_element_by_xpath("(//option[@value='April'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2010")
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(u"г. Город, ул. Улица_2, д. 2, оф. 1")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("1122334455")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(u"Это тест")
        # submit group creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.wd.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
