from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_check_mask(card_number_masked: str) -> None:
    assert get_mask_card_number(1234567890123456) == card_number_masked


def test_get_mask_card_number_check_len() -> None:
    assert get_mask_card_number(234567890123456) == "номер карты не равен 16 символам"


def test_get_mask_account_check_mask(account_number_masked: str) -> None:
    assert get_mask_account(73654108430135874305) == account_number_masked


def test_get_mask_account_check_len() -> None:
    assert get_mask_account(3654108430135874305) == "номер счета не равен 20 символам"
