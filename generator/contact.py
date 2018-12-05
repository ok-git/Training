from model.contact import Contact
from generator.generator_lib import random_day_of_month
from generator.generator_lib import random_month
from generator.generator_lib import random_year
from generator.generator_lib import random_string as rand_str
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:e", ["number of groups", "file", "add empty contact"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# Default values
n = 3
f = "data/contacts.json"
add_empty_contact = False

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a
    elif o == "-e":
        add_empty_contact = True

testdata = [Contact(
        firstname=rand_str("First_", 7, spaces=False),
        middlename=rand_str("Middle_", 7),
        lastname=rand_str("Last_", 7, spaces=False),
        title=rand_str("Title_", 7),
        company=rand_str("Company_", 7),
        address=rand_str("Addr_", 70, fixedlen=True, spaces=False),
        home=rand_str("H_", 9),
        mobile=rand_str("M_", 9),
        work=rand_str("W_", 9),
        fax=rand_str("F_", 7),
        email=rand_str("Em1_", 9, spaces=False),
        email2=rand_str("Em2_", 9, spaces=False),
        email3=rand_str("Em3_", 9, spaces=False),
        homepage=rand_str("Hp_", 15),
        bday=random_day_of_month(), bmonth=random_month(), byear=random_year(),
        aday=random_day_of_month(), amonth=random_month(), ayear=random_year(),
        address2=rand_str("Addr2_", 90, fixedlen=True),
        phone2=rand_str("Ph2_", 9),
        notes=rand_str("Notes_", 150, fixedlen=True))
    for i in range(n)
]

if add_empty_contact:
    testdata = [Contact(
        firstname="", middlename="", lastname="",
        title="", company="", address="",
        home="", mobile="", work="", fax="",
        email="", email2="", email3="", homepage="",
        bday="-", bmonth="-", byear="",
        aday="-", amonth="-", ayear="",
        address2="", phone2="", notes="")] + testdata

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
