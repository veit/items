import pytest


@pytest.fixture(name="ultimate_answer")
def ultimate_fixture():
    """The answer to the ultimate question"""
    return 42


def test_some_data(ultimate_answer):
    """Use fixture return value in a test."""
    assert ultimate_answer == 42
