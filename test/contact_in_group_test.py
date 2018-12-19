from model.contact import Contact
from model.group import Group
import random


def test_add_some_contact_to_some_group(app, db, ormdb):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(
            firstname="Петр",
            lastname="Петров",
            address="г. Город, ул. Улица, д. 1, оф. 305"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test Group to add Contact"))
    contact = random.choice(db.get_contacts_list())
    group = random.choice(db.get_group_list())
    app.contact.add_contact_to_group_by_id(contact, group)
    assert contact == list(filter(lambda x: x.id == contact.id, ormdb.get_contacts_in_group(group)))[0]


def test_del_some_contact_from_some_group(app, db, ormdb):
    if len(ormdb.get_groups_with_contacts()) == 0:
        test_add_some_contact_to_some_group(app, db, ormdb)
    group_to_disconnect = random.choice(ormdb.get_groups_with_contacts())
    old_contacts_in_group = ormdb.get_contacts_in_group(group_to_disconnect)
    contact_to_disconnect = random.choice(old_contacts_in_group)
    app.contact.disconnect_contact_from_group(contact_to_disconnect, group_to_disconnect)
    new_contacts_in_group = ormdb.get_contacts_in_group(group_to_disconnect)
    old_contacts_in_group.remove(contact_to_disconnect)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
