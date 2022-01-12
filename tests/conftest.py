import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                 help="Choose language. For ex.: ru, es, en, fr")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language}) # en-US
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)  # говорим WebDriver искать каждый элемент в течение 5 секунд
    yield browser
    print("\nquit browser..")
    browser.quit()
