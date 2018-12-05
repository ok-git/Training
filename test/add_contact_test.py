# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, data_contacts):
    contact = data_contacts
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# For memory
# Contact(
#        firstname="Петр",
#        middlename="Петрович",
#        lastname="Петров",
#        title="Директор",
#        company="ООО Хороший софт",
#        address="г. Город, ул. Улица, д. 1, оф. 305",
#        home="1234567",
#        mobile="2345678",
#        work="3456789",
#        fax="4567890",
#        email="email@goodsoft.ru",
#        email2="pr@goodsoft.ru",
#        email3="sales@goodsoft.ru",
#        homepage="www.goodsoft.ru",
#        bday="1",
#        bmonth="January",
#        byear="1970",
#        aday="2",
#        amonth="April",
#        ayear="2010",
#        address2="г. Город, ул. Улица_2, д. 2, оф. 1",
#        phone2="1122334455",
#        notes="Это тест")
