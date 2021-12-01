from Model.contact import Contact
from selenium.webdriver.support.ui import Select


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

    def edit_random(self, new_contact_params, index):
        wd = self.app.wd
        self.app.open_home_page()
        # Select contact
        wd.find_elements_by_name("selected[]")[index].click()
        # Edit selected contact
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact_params)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.addr)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

#def del_first_from_home_page(self):

    def del_random_from_home_page(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # Select contact
        wd.find_elements_by_name("selected[]")[index].click()
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
                cells = elements.find_elements_by_tag_name("td")
                id = elements.find_element_by_name("selected[]").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                addr = cells[3].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname, addr=addr,
                                                  all_phones=all_phones, all_emails=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_contact_from_edit_page(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_to_edit(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, addr=address, id=id,
                       homephone=homephone, mobile=mobile, workphone=workphone, phone2=phone2,
                       email1=email1, email2=email2, email3=email3)

    def delete_contact_by_id_from_hp(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        # Select contact
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        # Delete selected contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # self.app.assertRegexpMatches(self.app.close_alert_and_get_its_text(), r"^Delete 1 addresses[\s\S]$")
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, new_contact_params, id):
        wd = self.app.wd
        self.app.open_home_page()
        # Select contact
        index = self.find_contact_index_by_id(id)
        # Edit selected contact
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact_params)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def find_contact_index_by_id(self, id):
        wd = self.app.wd
        index = 0
        for elements in wd.find_elements_by_name("entry"):
            if elements.find_element_by_name("selected[]").get_attribute("value") != str(id):
                index = index + 1
            else:
                break
        return index

    def put_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        index = self.find_contact_index_by_id(contact_id)
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_value(group_id)
        wd.find_element_by_name("add").click()
        self.app.open_home_page()

    def delete_contact_from_group(self, group_id, contact_id):
        wd = self.app.wd
        wd.find_element_by_name("group").click()
        Select(wd.find_element_by_name("group")).select_by_value(group_id)
        index = self.find_contact_index_by_id(contact_id)
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_name("remove").click()
        self.app.open_home_page()



'''
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
'''
