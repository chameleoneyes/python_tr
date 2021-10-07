from selenium import webdriver


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def create_group(self, group):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()
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

    def return_page_group(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()
        # for delay
        wd.find_element_by_name("new")

    def login(self, login, pwd):
        wd = self.wd
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(pwd)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()
        # for delay
        wd.find_element_by_name("user")

    def clear_fixture(self):
        self.wd.quit()
