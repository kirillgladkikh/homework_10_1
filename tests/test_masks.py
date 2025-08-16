from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number_check_mask(card_number_masked):
    assert get_mask_card_number(1234567890123456) == card_number_masked


def test_get_mask_card_number_check_len():
    assert get_mask_card_number(234567890123456) == "номер карты не равен 16 символам"


# def test_get_mask_card_number_check_int():
#   assert get_mask_card_number('234567890123456') == 'номер карты не равен 16 символам'


def test_get_mask_account_check_mask(account_number_masked):
    assert get_mask_account(73654108430135874305) == account_number_masked


def test_get_mask_account_check_len():
    assert get_mask_account(3654108430135874305) == "номер счета не равен 20 символам"
