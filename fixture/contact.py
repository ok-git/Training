from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def remove_all_contacts_from_group(self, Group):
        wd = self.app.wd
        self.app.open_home_page()
        #select group by group_name
        Select(wd.find_element_by_name("group")).select_by_visible_text(Group.name)
        self.select_all_contacts()
        # remove contacts from group
        wd.find_element_by_name("remove").click()
        self.app.open_home_page()

    def select_all_contacts(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[2]").click()

    def add_all_contacts_to_group(self, Group):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_all_contacts()
        # select group by group_name
        Select(wd.find_element_by_name("to_group")).select_by_visible_text(Group.name)
        #add contacts to first group in the Add_group dropdown box
        wd.find_element_by_name("add").click()
        self.app.open_home_page()

    def edit_first_contact(self, new_contact_data):
        self.edit_contact_by_index(0, new_contact_data)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        # init edition
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        # accept contact edition
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.contacts_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # select contact
        wd.find_elements_by_name("selected[]")[index].click()
        # delete contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # accept deletion
        wd.switch_to.alert.accept()
        # Slowdown method to make deletion test more stable - begin
        wd.find_element_by_css_selector("div.msgbox")
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_xpath("//input[@value='Delete']")
        # Slowdown method to make deletion test more stable - end
        self.contacts_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        # select contact
        # wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        # delete contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # accept deletion
        wd.switch_to.alert.accept()
        # Slowdown method to make deletion test more stable - begin
        wd.find_element_by_css_selector("div.msgbox")
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_xpath("//input[@value='Delete']")
        # Slowdown method to make deletion test more stable - end
        self.contacts_cache = None


    def create(self, Contact):
        wd = self.app.wd
        self.app.open_home_page()
        # init creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(Contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contacts_cache = None

    def fill_contact_form(self, Contact):
        self.change_field_value("firstname", Contact.firstname)
        self.change_field_value("middlename", Contact.middlename)
        self.change_field_value("lastname", Contact.lastname)
        self.change_field_value("title", Contact.title)
        self.change_field_value("company", Contact.company)
        self.change_field_value("address", Contact.address)
        self.change_field_value("home", Contact.home)
        self.change_field_value("mobile", Contact.mobile)
        self.change_field_value("work", Contact.work)
        self.change_field_value("fax", Contact.fax)
        self.change_field_value("email", Contact.email)
        self.change_field_value("email2", Contact.email2)
        self.change_field_value("email3", Contact.email3)
        self.change_field_value("homepage", Contact.homepage)
        self.change_date_value("bday", Contact.bday)
        self.change_date_value("bmonth", Contact.bmonth)
        self.change_field_value("byear", Contact.byear)
        self.change_date_value("aday", Contact.aday)
        self.change_date_value("amonth", Contact.amonth)
        self.change_field_value("ayear", Contact.ayear)
        self.change_field_value("address2", Contact.address2)
        self.change_field_value("phone2", Contact.phone2)
        self.change_field_value("notes", Contact.notes)

    def change_date_value(self, date_field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(date_field_name).click()
            Select(wd.find_element_by_name(date_field_name)).select_by_visible_text(text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cache = None

    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contacts_cache = []
            for element in wd.find_elements_by_css_selector("tr[name*=entry]"):
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                # alternative method
                #lastname = element.find_element_by_css_selector("*:nth-of-type(2)").text
                #firstname = element.find_element_by_css_selector("*:nth-of-type(3)").text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contacts_cache.append(Contact(firstname=firstname,
                                                   lastname=lastname,
                                                   address=address,
                                                   all_emails_from_homepage=all_emails,
                                                   all_phones_from_homepage=all_phones,
                                                   id=id))
        return list(self.contacts_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        self.app.open_home_page()
        return Contact(
            firstname=firstname,
            lastname=lastname,
            address=address,
            home=home,
            mobile=mobile,
            work=work,
            email=email,
            email2=email2,
            email3=email3,
            phone2=phone2,
            id=id
            )
