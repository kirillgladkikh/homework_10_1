import pytest


@pytest.fixture
def card_number_masked():
    return '1234 56** **** 3456'


@pytest.fixture
def account_number_masked():
    return '**4305'


@pytest.fixture
def get_date_input():
    return '2024-03-11T02:26:18.671407'