from model.group import Group


def test_edit_name_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Change Name Only"))
    app.session.logout()


def test_edit_footer_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(footer="Change Footer Only"))
    app.session.logout()
