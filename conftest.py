import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="choose language ")
@pytest.fixture()
def browser(request):
    browser_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    print("/nstart browser")
    browser=webdriver.Chrome(options=options)
    yield browser
    print("/nquit browser")
    browser.quit()
