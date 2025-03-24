import pytest
from selene import browser
from selene.support.shared import config

@pytest.fixture(scope="session")
def setup_browser():
    # Настройка конфигурации браузера
    config.browser_name = 'chrome'
    config.window_width = 1000
    config.window_height = 500

    yield
    browser.quit()