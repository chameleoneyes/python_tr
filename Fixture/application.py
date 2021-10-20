from selenium import webdriver
from Fixture.session import SessionHelper
from Fixture.group import GroupHelper
from Fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
#        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        if wd.current_url != "http://localhost/addressbook/":
            wd.get("http://localhost/addressbook/")

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def clear_fixture(self):
        self.wd.quit()
