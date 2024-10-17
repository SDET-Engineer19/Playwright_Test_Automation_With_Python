import pytest


@pytest.fixture(scope="module")
def test_intialization():
    print("***************** TEST EXECUTION STARTED *****************************")
    yield
    print("***************** TEST EXECUTION ENDED *****************************")


@pytest.mark.usefixtures("test_intialization")
def test_m6():
    assert True


@pytest.mark.usefixtures("test_intialization")
def test_m7():
    courses = ["Playwright", "API Automation", "Kubernetes", "AWS"]
    assert len(courses) == 1
