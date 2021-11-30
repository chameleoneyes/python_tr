from Model.group import Group
import random
import string
import re


tdata = [
    Group(gname="", gheader="", gfooter=""),
    Group(gname="name1", gheader="header1", gfooter="footer1"),
    Group(gname="name2", gheader="header2", gfooter="footer2")
]

'''
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    s = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    s = s.strip()
    s = re.sub('\s+',' ', s)
    return prefix + s


tdata = [Group(gname="", gheader="", gfooter="")] + [
    Group(gname=random_string("name", 10), gheader=random_string("header", 5), gfooter=random_string("footer", 8))
    for i in range(5)
]

'''