from Fixture.orm import ORMfixture
import re
from Model.contact import Contact


# Задание №21: Переделать тесты для проверки информации о контактах на главной странице
def test_check_contacts_view(app):
    db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", pwd="")
    contacts_from_db = db.get_contact_list()
    contact_from_hp = app.contact.get_contact_list()
    for contact in contacts_from_db:
        contact.all_phones = merge_phones(contact)
        contact.all_emails = merge_emails(contact)
    for contact in contact_from_hp:
        contact.all_phones = clear_blank_phones_lines(contact.all_phones)
    assert sorted(contacts_from_db, key=Contact.con_id_fill) == sorted(contact_from_hp, key=Contact.con_id_fill)


def clear(string):
    return re.sub("[]() -]", "", string)


def clear_blank_phones_lines(string):
    return re.sub('\n+', '\n', string)


def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                                                filter(lambda x: x is not None, [contact.homephone, contact.mobile,
                                                                                 contact.workphone, contact.phone2]))))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                          [contact.email1, contact.email2, contact.email3])))





