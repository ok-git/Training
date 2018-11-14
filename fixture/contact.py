from selenium.webdriver.support.ui import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def remove_all_contacts_from_group(self):
        wd = self.app.wd
        self.app.open_home_page()
        Select(wd.find_element_by_name("group")).select_by_visible_text("Group2 Name")
        self.select_all_contacts()
        # remove contacts from group
        wd.find_element_by_name("remove").click()
        self.app.open_home_page()

    def select_all_contacts(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[2]").click()

    def add_all_contacts_to_group(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_all_contacts()
        #add contacts to first group in the Add_group dropdown box
        wd.find_element_by_name("add").click()
        self.app.open_home_page()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        # init edition
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # accept contact edition
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        #select first contact
        wd.find_element_by_name("selected[]").click()
        #delete contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #accept deletion
        wd.switch_to.alert.accept()
        self.app.open_home_page()

    def create(self, Contact):
        wd = self.app.wd
        self.app.open_home_page()
        # init creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(Contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

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
