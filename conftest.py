import json
import pytest
from Fixture.application import Application
import os.path
import importlib
import jsonpickle


fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as cf:
            target = json.load(cf)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, url=target["testUrl"])
    fixture.session.ensure_login(pwd=target["password"], login=target["username"])
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def f_exit():
        fixture.session.ensure_logout()
        fixture.clear_fixture()
    request.addfinalizer(f_exit)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            tdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, tdata, ids=[str(x) for x in tdata])
        elif fixture.startswith("json_"):
            tdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, tdata, ids=[str(x) for x in tdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).tdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())
