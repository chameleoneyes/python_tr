class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("home page").click()

    def edit_first(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # Select contact
        wd.find_element_by_name("selected[]").click()
        # Edit selected contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()

    def del_first1(self):
        wd = self.app.wd
        self.app.open_home_page()
        # Select contact
        wd.find_element_by_name("selected[]").click()
        # Delete selected contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # self.app.assertRegexpMatches(self.app.close_alert_and_get_its_text(), r"^Delete 1 addresses[\s\S]$")
        wd.switch_to_alert().accept()
        self.app.open_home_page()

    def del_first2(self):
        wd = self.app.wd
        self.app.open_home_page()
        # Select contact
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # Delete selected contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.app.open_home_page()
