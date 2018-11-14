from model.group import Group


def test_edit_name_first_group(app):
    app.group.edit_first_group(Group(name="Change Name Only"))


def test_edit_footer_first_group(app):
    app.group.edit_first_group(Group(footer="Change Footer Only"))
