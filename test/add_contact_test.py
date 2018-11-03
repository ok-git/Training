# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.add_contact(Contact(
                     firstname="Петр",
                     middlename="Петрович",
                     lastname="Петров",
                     title="Директор",
                     company="ООО Хороший софт",
                     address="г. Город, ул. Улица, д. 1, оф. 305",
                     home="1234567",
                     mobile="2345678",
                     work="3456789",
                     fax="4567890",
                     email="email@goodsoft.ru",
                     email2="pr@goodsoft.ru",
                     email3="sales@goodsoft.ru",
                     homepage="www.goodsoft.ru",
                     bday="1",
                     bmonth="January",
                     byear="1970",
                     aday="2",
                     amonth="April",
                     ayear="2010",
                     address2="г. Город, ул. Улица_2, д. 2, оф. 1",
                     phone2="1122334455",
                     notes="Это тест"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.add_contact(Contact(
                     firstname="",
                     middlename="",
                     lastname="",
                     title="",
                     company="",
                     address="",
                     home="",
                     mobile="",
                     work="",
                     fax="",
                     email="",
                     email2="",
                     email3="",
                     homepage="",
                     bday="-",
                     bmonth="-",
                     byear="",
                     aday="-",
                     amonth="-",
                     ayear="",
                     address2="",
                     phone2="",
                     notes=""))
    app.session.logout()
