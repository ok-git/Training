# -*- coding: utf-8 -*-
from model.contact import Contact
from generator.generator_lib import random_day_of_month
from generator.generator_lib import random_month
from generator.generator_lib import random_year
from generator.generator_lib import random_string as rand_str


constant = [
    Contact(
            firstname="Петр",
            lastname="Петров",
            address="г. Город, ул. Улица, д. 1, оф. 305"),
    Contact(
            firstname="Василий",
            lastname="Васильев",
            address="г. Город-2, ул. Улица-2, д. 2, оф. 306")
]

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
