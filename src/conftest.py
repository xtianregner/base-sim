import pytest

@pytest.fixture
def sample_fixture():
    return "Hello, World!"

def pytest_configure():
    pass

def pytest_unconfigure():
    pass