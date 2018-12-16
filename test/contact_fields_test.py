import re
from random import randrange
from model.contact import Contact


def test_contact_fields_comparison(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            firstname="Петр",
            lastname="Петров",
            address="г. Город, ул. Улица, д. 1, оф. 305",
            home="1234567",
            mobile="2345678",
            work="3456789",
            email="email@goodsoft.ru",
            email2="pr@goodsoft.ru",
            email3="sales@goodsoft.ru"))
    contacts_from_home_page = app.contact.get_contacts_list()
    contacts_from_db = db.get_contacts_list()
    for contact in contacts_from_db:
        contact.all_phones_from_homepage = merge_phones_like_on_home_page(contact)
        contact.all_emails_from_homepage = merge_emails_like_on_home_page(contact)
    assert sorted(contacts_from_home_page, key=Contact.id_or_max) == sorted(contacts_from_db, key=Contact.id_or_max)
    if check_ui:
        index = randrange(app.contact.count())
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
        contact_from_home_page = app.contact.get_contacts_list()[index]
        assert contact_from_home_page.firstname == contact_from_edit_page.firstname
        assert contact_from_home_page.lastname == contact_from_edit_page.lastname
        assert contact_from_home_page.address == contact_from_edit_page.address
        assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_home_page(contact_from_edit_page)
        assert contact_from_home_page.all_emails_from_homepage == merge_emails_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
