from model.group import Group


def test_edit_name_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test Name", footer="Test Footer"))
    app.group.edit_first_group(Group(name="Change Name Only"))

