import pytest

from src.masks import get_mask_cards, get_mask_account


def test_get_mask_cards(cards):
    assert get_mask_cards("7000792289606361") == "7000 79** **** 6361"


@pytest.mark.parametrize("cards, expected", [("", ""), ("700079228960636", ""), ("700079228960636543", ""),])
def test_get_mask_cards_parametrize(cards, expected):
    assert get_mask_cards(cards) == expected


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"


@pytest.mark.parametrize("account, expected", [("", ""), ("7365410843013587430", ""), ("7365410843013587430523", ""),])
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected
