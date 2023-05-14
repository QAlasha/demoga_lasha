from selene import browser
import pytest


@pytest.fixture(autouse=True)
def browser_open():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 700
    browser.config.window_height = 1080
    yield
    browser.quit()
