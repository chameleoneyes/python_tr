from sys import maxsize


class Group:
    def __init__(self, gname=None, gheader=None, gfooter=None, gid=None):
        self.gname = gname
        self.gheader = gheader
        self.gfooter = gfooter
        self.id = gid

    def __repr__(self):
        return "%s:%s" % (self.id, self.gname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.gname == other.gname

    def gr_id_fill(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
