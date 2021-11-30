from Model.group import Group


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
        self.group_cache = None

    def edit_first(self, new_group_param):
        self.edit_random(new_group_param, 0)

    def edit_random(self, new_group_param, index):
        wd = self.app.wd
        self.open_page_group()
        self.select_group_by_index(index)
        # Edit selected group
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_param)
        wd.find_element_by_name("update").click()
        # check
        self.return_page_group()
        self.group_cache = None

    def edit_group_by_id(self, new_group_param, id):
        wd = self.app.wd
        self.open_page_group()
        self.select_group_by_id(id)
        # Edit selected group
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_param)
        wd.find_element_by_name("update").click()
        # check
        self.return_page_group()
        self.group_cache = None

    def del_first(self):
        self.del_random(0)

    def del_random(self, index):
        wd = self.app.wd
        self.open_page_group()
        self.select_group_by_index(index)
        # Delete selected group
        wd.find_element_by_name("delete").click()
        self.return_page_group()
        self.group_cache = None

    def fill_group_form(self, group):
#        wd = self.app.wd
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
        if not (wd.current_url.endswith("/group.php") and wd.find_element_by_name("new")):
            wd.find_element_by_link_text("groups").click()

    def return_page_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
        # for delay
        wd.find_element_by_name("new")

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def count(self):
        wd = self.app.wd
        self.open_page_group()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_page_group()
            self.group_cache = []
            for elements in wd.find_elements_by_css_selector("span.group"):
                text = elements.text
                id = elements.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(gname=text, gid=id))
        return list(self.group_cache)

    def del_group_by_id(self, id):
        wd = self.app.wd
        self.open_page_group()
        self.select_group_by_id(id)
        # Delete selected group
        wd.find_element_by_name("delete").click()
        self.return_page_group()
        self.group_cache = None

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
