import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="es",
                     help="Choose browser: language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = webdriver.Chrome()
    if language == "es":
        print("\nstart chrome browser for test..")
        browser.get('http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/')
    elif language != "fr":
        print("\nlanguage should be es or fr")
    else:
        print("\nstart chrome browser for test..")
        browser.get('http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/')
    yield browser
    print("\nquit browser..")
    browser.quit()
