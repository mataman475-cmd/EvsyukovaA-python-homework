import pytest
from string_utils import StringUtils

utils = StringUtils()

# --- Тесты для capitalize ---


def test_capitalize_normal():
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_empty_string():
    assert utils.capitalize("") == ""


def test_capitalize_already_capitalized():
    assert utils.capitalize("Skypro") == "Skypro"

# --- Тесты для trim ---


def test_trim_with_spaces():
    assert utils.trim("   skypro") == "skypro"


def test_trim_no_spaces():
    assert utils.trim("skypro") == "skypro"


def test_trim_only_spaces():
    assert utils.trim("     ") == ""

# --- Тесты для contains ---


def test_contains_symbol_exists():
    assert utils.contains("SkyPro", "S") is True


def test_contains_with_spaces():
    assert utils.contains("04 апреля 2023", " ") is True


def test_contains_symbol_not_exists():
    assert utils.contains("SkyPro", "U") is False


def test_contains_empty_string():
    assert utils.contains("", "a") is False


# --- Тесты для delete_symbol ---

def test_delete_symbol_single_char():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_substring():
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_not_found():
    # Функция должна вернуть исходную строку, если символ не найден
    result = utils.delete_symbol("SkyPro", "Z")
    assert result == "SkyPro"


def test_delete_all_occurrences():
    assert utils.delete_symbol("banana", "a") == "bnn"
