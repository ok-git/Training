# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Group2 Name", header="Group2 Header", footer="Group2 Footer"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
