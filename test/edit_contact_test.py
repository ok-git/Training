# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group


def test_edit_firstname_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            firstname="Петр",
            lastname="Петров"))
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="Василий", lastname="Васильев")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_group_membership_for_all_contacts(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(
#            firstname="Петр",
#            middlename="Петрович",
#            lastname="Петров"))
#    app.group.create(Group(name="Test Name"))
#    app.contact.add_all_contacts_to_group(Group(name="Test Name"))
#    app.contact.remove_all_contacts_from_group(Group(name="Test Name"))
