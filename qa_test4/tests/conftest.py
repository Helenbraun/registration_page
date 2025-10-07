
import pytest
from selene.support.shared import browser

from tests.config import Config

config = Config()

@pytest.fixture(scope='function', autouse=True)
def in_browser():
    browser.config.window_height = config.window_height
    browser.config.window_width =config.window_width
    browser.config.base_url = config.base_url
    browser.config.timeout = config.timeout


    yield