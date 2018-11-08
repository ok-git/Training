# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(
                     firstname="Василий",
                     middlename="Васильевич",
                     lastname="Васильев",
                     title="Бухгалтер",
                     company="ООО То же Хороший софт",
                     address="г. Город-2, ул. Улица-2, д. 2, оф. 306",
                     home="9234567",
                     mobile="9345678",
                     work="9456789",
                     fax="9567890",
                     email="email@2goodsoft.ru",
                     email2="pr@2goodsoft.ru",
                     email3="sales@2goodsoft.ru",
                     homepage="www.2goodsoft.ru",
                     bday="2",
                     bmonth="May",
                     byear="1971",
                     aday="5",
                     amonth="June",
                     ayear="2012",
                     address2="г. Город-2, ул. Улица_3, д. 3, оф. 2",
                     phone2="9122334455",
                     notes="Это редакция контакта"))
    app.session.logout()


def test_add_all_contacts_to_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_all_contacts_to_group()
    app.session.logout()


