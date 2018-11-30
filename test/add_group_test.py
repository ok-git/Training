# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from test.address_book_lib import random_string as rand_str


testdata = [Group(name="", header="", footer="")]+[
    Group(name=rand_str("name_", 10, punctuation=True),
          header=rand_str("header_", 15, punctuation=True),
          footer=rand_str("footer_", 15, punctuation=True))
    for i in range(5)
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
