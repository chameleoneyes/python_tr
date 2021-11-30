from Model.contact import Contact
import pytest
import random
import string
import re
import getopt
import sys
import os.path
import jsonpickle


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


num = 6
ff = "data/contacts.json"

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


def random_phone(maxlen):
    symbols = string.digits + " +-()"
    n = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    n = n.strip()
    n = re.sub('\s+',' ', n)
    return n


def random_email(domain_len, bodylen):
    symbols = string.ascii_letters + string.digits
    body = "".join([random.choice(symbols) for i in range(random.randrange(bodylen))])
    domain = "".join([random.choice(string.ascii_lowercase) for i in range(random.randrange(domain_len))])
    return body + "@" + domain + "." + "".join([random.choice(string.ascii_lowercase) for i in range(random.randrange(2)+1)])


tdata = [Contact(firstname=random_string("name", 10), lastname=random_string("lastname", 10), addr=random_string("", 20),
                 homephone=random_phone(10), mobile=random_phone(12), workphone=random_phone(10), phone2=random_phone(15),
                 email1=random_email(10, 5), email2=random_email(15, 8), email3=random_email(20, 15))
         for i in range(5)
         ]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ff)

with open(file, "w") as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(tdata))
