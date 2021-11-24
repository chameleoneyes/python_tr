from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, addr=None, company=None, mobile=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.mobile = mobile
        self.id = id
        self.addr = addr

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and (self.firstname == other.firstname or
                self.firstname is None or other.firstname is None) and (self.lastname == other.lastname or self.lastname
                is None or other.lastname is None) and (self.addr == other.addr or self.addr is None or other.addr is None))

    def con_id_fill(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize