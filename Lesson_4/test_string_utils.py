from string_utils import StringUtils

string_utils = StringUtils()

def test_all_lowercase_letters():
    string_utils = StringUtils()
    res = string_utils.capitilize("my first test")
    assert res == "My first test"

def test_all_lowercase_letters_except_first():
    string_utils = StringUtils()
    res = string_utils.capitilize("My first test")
    assert res == "My first test"   

def test_empty_string():
    string_utils = StringUtils()
    res = string_utils.capitilize("")
    assert res == ""

def test_only_spaces():
    string_utils = StringUtils()
    res = string_utils.capitilize("   ")
    assert res == "   "

def test_only_numbers():
    string_utils = StringUtils()
    res = string_utils.capitilize("12345")
    assert res == "12345"

def test_without_argument():
    string_utils = StringUtils()
    res = string_utils.capitilize()
    assert res == "   "             

def test_all_lowercase_letters_except_first_number():
    string_utils = StringUtils()
    res = string_utils.capitilize("5my first test")
    assert res == "5My first test"

def test_all_capitals_letters_except_first_lowercase():
    string_utils = StringUtils()
    res = string_utils.capitilize("sKYPRO")
    assert res == "SKYPRO"

def test_spaces_before():
    string_utils = StringUtils()
    res = string_utils.trim("      My first test")
    assert res == "My first test"

def test_without_spaces_before():
    string_utils = StringUtils()
    res = string_utils.trim("My first test")
    assert res == "My first test"

def test_string_to_list():
    string_utils = StringUtils()
    res = string_utils.to_list("My,first,test")
    assert res == ["My", "first", "test"]
