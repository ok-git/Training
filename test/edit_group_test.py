from model.group import Group
import random


def test_edit_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test Name", footer="Test Footer"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group.name = "Change Name Only"
    app.group.edit_group_by_id(group)
    new_groups = db.get_group_list()
    # assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
