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
    res = string_utils.capitilize()
    assert res == "   "             

def test_capitilize_all_lowercase_letters_except_first_number():
    string_utils = StringUtils()
    res = string_utils.capitilize("5my first test")
    assert res == "5My first test"

def test_capitilize_all_capitals_letters_except_first_lowercase():
    string_utils = StringUtils()
    res = string_utils.capitilize("sKYPRO")
    assert res == "SKYPRO"

def test_trim_spaces_before():
    string_utils = StringUtils()
    res = string_utils.trim("      My first test")
    assert res == "My first test"

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

def test_delete_symbol_five_lowercase_symbol():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("My first test 99", "first")
    assert res == "My  test 99"

def test_delete_symbol_one_capital_symbol():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("My first Mest 99", "M")
    assert res == "y first est 99"   

def test_delete_symbol_five_lowercase_symbol_and_number():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("My first 99 test", "first 99")
    assert res == "My  test"