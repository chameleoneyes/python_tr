

class Group:
    def __init__(self, gname=None, gheader=None, gfooter=None, gid=None):
        self.gname = gname
        self.gheader = gheader
        self.gfooter = gfooter
        self.id = gid

    def __repr__(self):
        return "%s:%s" % (self.id, self.gname)

    def __eq__(self, other):
        return self.id == other.id and self.gname == other.gname
