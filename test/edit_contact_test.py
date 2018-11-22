# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group


def test_edit_firstname_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            firstname="Петр",
            middlename="Петрович",
            lastname="Петров"))
    app.contact.edit_first_contact(Contact(firstname="Василий"))


#def test_modify_group_membership_for_all_contacts(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(
#            firstname="Петр",
#            middlename="Петрович",
#            lastname="Петров"))
#    app.group.create(Group(name="Test Name"))
#    app.contact.add_all_contacts_to_group(Group(name="Test Name"))
#    app.contact.remove_all_contacts_from_group(Group(name="Test Name"))
