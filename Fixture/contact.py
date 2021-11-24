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

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("company", contact.company)
        self.change_field_value("mobile", contact.mobile)

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

    def del_first_from_edit_form(self):
        wd = self.app.wd
        self.app.open_home_page()
        # Select contact
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # Delete selected contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.app.open_home_page()

    def del_all(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        contactlist = []
        for elements in wd.find_elements_by_name("entry"):
#            text = elements.text
            id = elements.find_element_by_name("selected[]").get_attribute("value")
#            firstname = elements.find_element_by_xpath("//input[@value='%s']/following-sibling:://td[3]" % str(id)).text
            firstname = elements.find_element_by_xpath(".//td[3]").text
            contactlist.append(Contact(id=id, firstname=firstname))
        return contactlist
