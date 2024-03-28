import pytest
from string_utils import StringUtils

string_utils = StringUtils()


def test_capitilize_all_lowercase_letters():
    string_utils = StringUtils()
    res = string_utils.capitilize("my first test")
    assert res == "My first test"


def test_capitilize_all_lowercase_letters_except_first():
    string_utils = StringUtils()
    res = string_utils.capitilize("My first test")
    assert res == "My first test"


def test_capitilize_empty_string():
    string_utils = StringUtils()
    res = string_utils.capitilize("")
    assert res == ""


def test_capitilize_only_spaces():
    string_utils = StringUtils()
    res = string_utils.capitilize("   ")
    assert res == "   "


def test_capitilize_only_numbers():
    string_utils = StringUtils()
    res = string_utils.capitilize("12345")
    assert res == "12345"


def test_capitilize_without_argument():
    string_utils = StringUtils()
    with pytest.raises(TypeError):
        string_utils.capitilize()


@pytest.mark.xfail
def test_capitilize_all_lowercase_letters_except_first_number():
    string_utils = StringUtils()
    res = string_utils.capitilize("5my first test")
    assert res == "5My first test"


@pytest.mark.xfail
def test_capitilize_all_capitals_letters_except_first_lowercase():
    string_utils = StringUtils()
    res = string_utils.capitilize("sKYPRO")
    assert res == "SKYPRO"


@pytest.mark.test_trim     # декоратор для тестов trim
def test_trim_spaces_before():
    string_utils = StringUtils()
    res = string_utils.trim("      My first test")
    assert res == "My first test"


@pytest.mark.test_trim      # декоратор для тестов trim
def test_trim_without_spaces_before():
    string_utils = StringUtils()
    res = string_utils.trim("My first test")
    assert res == "My first test"


def test_string_to_list():
    string_utils = StringUtils()
    res = string_utils.to_list("My,first,test")
    assert res == ["My", "first", "test"]


def test_string_with_numbers_to_list():
    string_utils = StringUtils()
    res = string_utils.to_list("My,first,test99,7,35,156")
    assert res == ["My", "first", "test99", "7", "35", "156"]


def test_string_with_numbers_and_delimeter_to_list():
    string_utils = StringUtils()
    res = string_utils.to_list("My;first;test99;7;35;156", ";")
    assert res == ["My", "first", "test99", "7", "35", "156"]


def test_string_to_list_empty_string():
    string_utils = StringUtils()
    res = string_utils.to_list("")
    assert res == []


def test_string_to_list_one_symbol():
    string_utils = StringUtils()
    res = string_utils.to_list("M")
    assert res == ["M"]


def test_contains_capitals_symbol():
    string_utils = StringUtils()
    res = string_utils.contains("My first Test 99", "T")
    assert res == True


def test_contains_lowercase_symbol_():
    string_utils = StringUtils()
    res = string_utils.contains("My first Test 99", "f")
    assert res == True


def test_contains_number():
    string_utils = StringUtils()
    res = string_utils.contains("My first Test9", "9")
    assert res == True


def test_not_contains_symbol():
    string_utils = StringUtils()
    res = string_utils.contains("My first Test 99", "V")
    assert res == False


@pytest.mark.test_delete      # декоратор для тестов delete
def test_delete_symbol_five_lowercase_symbol():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("My first test 99", "first")
    assert res == "My  test 99"


@pytest.mark.test_delete       # декоратор для тестов delete
def test_delete_symbol_one_capital_symbol():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("My first Mest 99", "M")
    assert res == "y first est 99"


@pytest.mark.test_delete       # декоратор для тестов delete
def test_delete_symbol_four_lowercase_symbol_and_number():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("My first test 99", "test 99")
    assert res == "My first "


@pytest.mark.test_starts
def test_starts_with_symbol():
    string_utils = StringUtils()
    res = string_utils.starts_with("My first test", "M")
    assert res == True


@pytest.mark.test_starts
def test_starts_with_number():
    string_utils = StringUtils()
    res = string_utils.starts_with("1my first test", "1")
    assert res == True


@pytest.mark.test_starts
def test_not_starts_with_symbol():
    string_utils = StringUtils()
    res = string_utils.starts_with("My first test", "e")
    assert res == False


# ниже декоратор для тестов end_with, объединили три теста в один с параметрами
@pytest.mark.parametrize('str1, symbol, result', [("Test", "t", True), ("Te99", "99", True), ("Sec", "m", False)] )
def test_end_with(str1, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(str1, symbol)
    assert res == result


# ниже декоратор для тестов is_empty, объединили три теста в один с параметрами
@pytest.mark.parametrize('str2, result', [("", True), ("   ", True), ("My", False)] )
def test_is_empty(str2, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(str2)
    assert res == result


def test_list_to_string_symbols():
    string_utils = StringUtils()
    res = string_utils.list_to_string(["My", "first", "test"])
    assert res == ("My, first, test")


def test_list_to_string_symbols_joiner():
    string_utils = StringUtils()
    res = string_utils.list_to_string(["My", "first", "test"], " ")
    assert res == ("My first test")


def test_list_to_string_symbols_numbers_joiner():
    string_utils = StringUtils()
    res = string_utils.list_to_string(["My", "first", "test", "11"], " ")
    assert res == ("My first test 11")


def test_list_to_string_empty_list():
    string_utils = StringUtils()
    res = string_utils.list_to_string([])
    assert res == ("")
