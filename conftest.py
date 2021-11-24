import pytest
from Fixture.application import Application


fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(pwd="secret", login="admin")
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def f_exit():
        fixture.session.ensure_logout()
        fixture.clear_fixture()
    request.addfinalizer(f_exit)
    return fixture