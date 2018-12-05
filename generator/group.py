from generator.generator_lib import random_string as rand_str
from model.group import Group
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:e", ["number of groups", "file", "add empty group"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# Default values
n = 3
f = "data/groups.json"
add_empty_group = False

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a
    elif o == "-e":
        add_empty_group = True

testdata = [Group(
        name=rand_str("name_", 10, spaces=False),
        header=rand_str("header_", 15),
        footer=rand_str("footer_", 15))
    for i in range(n)
]

if add_empty_group:
    testdata = [Group(name="", header="", footer="")] + testdata


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
