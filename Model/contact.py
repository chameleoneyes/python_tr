from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, addr=None, company=None, id=None,
                 mobile=None, homephone=None, workphone=None, phone2=None, all_phones=None,
                 email1=None, email2=None, email3=None, all_emails=None):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.mobile = mobile
        self.homephone = homephone
        self.workphone = workphone
        self.phone2 = phone2
        self.id = id
        self.addr = addr
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.all_phones = all_phones
        self.all_emails = all_emails

    def __repr__(self):
        return "%s:%s;%s;%s,%s" % (self.id, self.firstname, self.lastname, self.mobile, self.email1)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and (self.firstname == other.firstname or
                self.firstname is None or other.firstname is None) and (self.lastname == other.lastname or self.lastname
                is None or other.lastname is None) and (self.addr == other.addr or self.addr is None or other.addr is None))

    def con_id_fill(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize