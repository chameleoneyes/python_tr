from Model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, new_contact_params):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(new_contact_params)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def edit_first(self, new_contact_params):
        wd = self.app.wd
        self.app.open_home_page()
        # Select contact
        wd.find_element_by_name("selected[]").click()
        # Edit selected contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_params)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.addr)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def del_first_from_home_page(self):
        wd = self.app.wd
        self.app.open_home_page()
        # Select contact
        wd.find_element_by_name("selected[]").click()
        # Delete selected contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # self.app.assertRegexpMatches(self.app.close_alert_and_get_its_text(), r"^Delete 1 addresses[\s\S]$")
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None

    def del_first_from_edit_form(self):
        wd = self.app.wd
        self.app.open_home_page()
        # Select contact
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # Delete selected contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.app.open_home_page()
        self.contact_cache = None

    def del_all(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for elements in wd.find_elements_by_name("entry"):
                id = elements.find_element_by_name("selected[]").get_attribute("value")
                firstname = elements.find_element_by_xpath(".//td[3]").text
                lastname = elements.find_element_by_xpath(".//td[2]").text
                addr = elements.find_element_by_xpath(".//td[4]").text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname, addr=addr))
        return list(self.contact_cache)
