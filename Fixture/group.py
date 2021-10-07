

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_page_group()
        # group creation
        wd.find_element_by_name("new").click()
        # filling forms
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.gname)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.gheader)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.gfooter)
        wd.find_element_by_name("submit").click()
        # check
        self.return_page_group()

    def open_page_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_page_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
        # for delay
        wd.find_element_by_name("new")