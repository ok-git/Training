from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            firstname="Петр",
            middlename="Петрович",
            lastname="Петров"))
    app.contact.delete_first_contact()
