

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, new_group_param):
        wd = self.app.wd
        self.open_page_group()
        # group creation
        wd.find_element_by_name("new").click()
        # filling forms
        self.fill_group_form(new_group_param)
        wd.find_element_by_name("submit").click()
        # check
        self.return_page_group()

    def edit_first(self, new_group_param):
        wd = self.app.wd
        self.open_page_group()
        self.select_first_group()
        # Edit selected group
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_param)
        wd.find_element_by_name("update").click()
        # check
        self.return_page_group()

    def del_first(self):
        wd = self.app.wd
        self.open_page_group()
        self.select_first_group()
        # Delete selected group
        wd.find_element_by_name("delete").click()
        self.return_page_group()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.gname)
        self.change_field_value("group_header", group.gheader)
        self.change_field_value("group_footer", group.gfooter)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_page_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_page_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
        # for delay
        wd.find_element_by_name("new")

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
