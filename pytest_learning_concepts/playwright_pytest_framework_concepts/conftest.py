from lib2to3.fixes.fix_input import context

import pytest


@pytest.fixture(scope="session")
def set_up(page):
    page.goto("/")
    page.set_default_timeout(3000)

    yield page
    page.close()
