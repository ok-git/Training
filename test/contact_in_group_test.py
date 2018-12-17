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
