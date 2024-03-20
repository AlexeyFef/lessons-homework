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

def test_all_lowercase_letters_except_first_number():
    string_utils = StringUtils()
    res = string_utils.capitilize("9my first test")
    assert res == "9My first test"    

def test_all_capitals_letters_except_first_lowercase():
    string_utils = StringUtils()
    res = string_utils.capitilize("mY FIRST TEST")
    assert res == "MY FIRST TEST"
