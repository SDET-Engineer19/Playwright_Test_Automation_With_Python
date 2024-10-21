import pytest


def test_m1():
    assert True


def test_m2():
    assert True


def test_m3():
    a = 3
    b = 5
    assert a + 2 == b, "Test Failed"
    assert a + 2 == b, "a is not eq to b"


def test_m4():
    name = "playwright"
    assert name.upper() == "PLAYWRIGHT", "name is not eq to Selenium Keyword"


def test_m5():
    courses = ["PlayWright", "API Automation", "Kubernetes", "AWS"]
    assert len(courses) > 2
