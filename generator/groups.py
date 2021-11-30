import jsonpickle

from Model.group import Group
import random
import string
import re
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


num = 5
ff = "data/groups.json"

for o, a in opts:
    if o == "-n":
        num = int(a)
    elif o == "-f":
        ff = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    s = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    s = s.strip()
    s = re.sub('\s+',' ', s)
    return prefix + s


tdata = [Group(gname="", gheader="", gfooter="")] + [
    Group(gname=random_string("name", 10), gheader=random_string("header", 5), gfooter=random_string("footer", 8))
    for i in range(num)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ff)

with open(file, "w") as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(tdata))
