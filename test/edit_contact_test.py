# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_firstname_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="Василий"))
    app.session.logout()


def test_add_all_contacts_to_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_all_contacts_to_group()
    app.session.logout()


def test_remove_all_contacts_from_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.remove_all_contacts_from_group()
    app.session.logout()
