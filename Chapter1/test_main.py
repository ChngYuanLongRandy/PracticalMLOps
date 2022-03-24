import pytest
from main import simple_function


def test_simple_function():
    assert simple_function(1, 1) == 2
    assert simple_function(-1, -1) == -2
    assert simple_function(10, -10) == 0
