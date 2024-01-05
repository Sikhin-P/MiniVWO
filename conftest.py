import pytest
from helpers.browsers import browsers


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='Chrome', help="Browser Options")


@pytest.fixture(scope='session', autouse=True)
def browser(request):
    browser_option = request.config.getoption('--browser')
    return browser_option


@pytest.fixture(scope='session')
def driver(browser):
    _driver = browsers(browser)
    return _driver()
