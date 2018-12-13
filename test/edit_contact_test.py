# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(
            firstname="Петр",
            lastname="Петров",
            address="г. Город, ул. Улица, д. 1, оф. 305"))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    # index = randrange(len(old_contacts))
    contact.firstname = "Андрей"
    contact.lastname ="Андреев"
    contact.address = "г. Город, ул. Улица, д. 1, оф. 305"
    # contact.id = old_contacts[index].id
    app.contact.edit_contact_by_id(contact)
    new_contacts = db.get_contacts_list()
    # assert len(old_contacts) == len(new_contacts)
    # old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(),
                                                                     key=Contact.id_or_max)
