# -*- coding: utf-8 -*-
from generator.generator_lib import random_string as rand_str
from model.group import Group


constant = [
    Group(name="Name_1", header="Header_1", footer="Footer_1"),
    Group(name="Name_2", header="Header_2", footer="Footer_2")
]

testdata = [Group(name="", header="", footer="")]+[
    Group(name=rand_str("name_", 10, spaces=False),
          header=rand_str("header_", 15),
          footer=rand_str("footer_", 15))
    for i in range(5)
]

