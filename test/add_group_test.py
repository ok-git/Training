# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def var_or_fixed(maxlen, fixedlen):
    if fixedlen:
        return maxlen
    else:
        return random.randrange(maxlen)


def random_string(prefix, maxlen, fixedlen=False):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(var_or_fixed(maxlen, fixedlen))])
# + string.punctuation


testdata = [Group(name="", header="", footer="")]+[
    Group(name=random_string("name_", 10),
          header=random_string("header_", 15),
          footer=random_string("footer_", 15))
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
