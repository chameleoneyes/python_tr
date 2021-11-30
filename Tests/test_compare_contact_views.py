import re


def test_compare_contact_views(app, index=4):
    contact_from_hp = app.contact.get_contact_list()[index]
    contact_from_ep = app.contact.get_contact_from_edit_page(index)
    assert contact_from_hp.firstname == contact_from_ep.firstname
    assert contact_from_hp.lastname == contact_from_ep.lastname
    assert contact_from_hp.addr == contact_from_ep.addr
    assert contact_from_hp.all_phones == merge_phones(contact_from_ep)
    assert contact_from_hp.all_emails == merge_emails(contact_from_ep)


# Clear special symbols from phone nums
def clear(string):
    return re.sub("[]() -]", "", string)


def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                                                filter(lambda x: x is not None, [contact.homephone, contact.mobile,
                                                                                 contact.workphone, contact.phone2]))))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                          [contact.email1, contact.email2, contact.email3])))
