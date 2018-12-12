from model.group import Group
import random


def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test Name"))
    old_groups = db.get_group_list()
    # index = randrange(len(old_groups))
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    # assert len(old_groups) - 1 == len(new_groups)
    # old_groups[index:index+1] = []
    old_groups.remove(group)
    assert old_groups == new_groups
