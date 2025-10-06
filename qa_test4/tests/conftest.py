from os import getenv

import _pytest
import pytest
from selene.support.shared import browser
import os


@pytest.fixture(scope='function')
def in_browser():
    browser.config.window_height = os.getenv('height', 1024)
    browser.config.window_width = os.getenv('width', 768)
    browser.config.base_url = os.getenv('base_url', 'https://demoqa.com')

    yield