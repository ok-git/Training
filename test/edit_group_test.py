from model.group import Group


def test_edit_name_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test Name", footer="Test Footer"))
    old_groups = app.group.get_group_list()
    group = Group(name="Change Name Only")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
