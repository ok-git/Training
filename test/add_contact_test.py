# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from test.address_book_lib import random_day_of_month
from test.address_book_lib import random_month
from test.address_book_lib import random_year
from test.address_book_lib import random_string as rand_str


testdata = [Contact(
        firstname="", middlename="", lastname="",
        title="", company="", address="",
        home="", mobile="", work="", fax="",
        email="", email2="", email3="", homepage="",
        bday="-", bmonth="-", byear="",
        aday="-", amonth="-", ayear="",
        address2="", phone2="", notes="")]+[
    Contact(
        firstname=rand_str("First_", 7, spaces=False),
        middlename=rand_str("Middle_", 7),
        lastname=rand_str("Last_", 7, spaces=False),
        title=rand_str("Title_", 7),
        company=rand_str("Company_", 7),
        address=rand_str("Addr_", 70, fixedlen=True, spaces=False),
        home=rand_str("H_", 9),
        mobile=rand_str("M_", 9),
        work=rand_str("W_", 9),
        fax=rand_str("F_", 7),
        email=rand_str("Em1_", 9, spaces=False),
        email2=rand_str("Em2_", 9, spaces=False),
        email3=rand_str("Em3_", 9, spaces=False),
        homepage=rand_str("Hp_", 15),
        bday=random_day_of_month(), bmonth=random_month(), byear=random_year(),
        aday=random_day_of_month(), amonth=random_month(), ayear=random_year(),
        address2=rand_str("Addr2_", 90, fixedlen=True),
        phone2=rand_str("Ph2_", 9),
        notes=rand_str("Notes_", 150, fixedlen=True))
    for i in range(3)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
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
