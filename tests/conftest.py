import pytest


@pytest.fixture
def card_number_masked():
    return '1234 56** **** 3456'


@pytest.fixture
def account_number_masked():
    return '**4305'