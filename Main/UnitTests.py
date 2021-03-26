import re
import unittest


class TestStringMethods(unittest.TestCase):

    # Setting up for the test
    def setUp(self):
        pass

    # Cleaning up after the test
    def tearDown(self):
        pass

    def test_empty(self):
        self.assertFalse(check_valid_name(''))

    def test_special_01(self):
        self.assertFalse(check_valid_name('~'))

    def test_special_02(self):
        self.assertFalse(check_valid_name('@'))

    def test_special_03(self):
        self.assertFalse(check_valid_name('#'))

    def test_special_04(self):
        self.assertFalse(check_valid_name('$'))

    def test_special_05(self):
        self.assertFalse(check_valid_name('%'))

    def test_special_06(self):
        self.assertFalse(check_valid_name('^'))

    def test_special_07(self):
        self.assertFalse(check_valid_name('&'))

    def test_special_08(self):
        self.assertFalse(check_valid_name('*'))

    def test_special_09(self):
        self.assertFalse(check_valid_name('('))

    def test_special_10(self):
        self.assertFalse(check_valid_name(')'))

    def test_special_11(self):
        self.assertFalse(check_valid_name('_'))

    def test_special_12(self):
        self.assertFalse(check_valid_name('+'))

    def test_special_13(self):
        self.assertFalse(check_valid_name('{'))

    def test_special_14(self):
        self.assertFalse(check_valid_name('}'))

    def test_special_15(self):
        self.assertFalse(check_valid_name(':'))

    def test_special_16(self):
        self.assertFalse(check_valid_name('™'))

    def test_special_17(self):
        self.assertFalse(check_valid_name('|'))

    def test_special_18(self):
        self.assertFalse(check_valid_name('<'))

    def test_special_19(self):
        self.assertFalse(check_valid_name('>'))

    def test_special_20(self):
        self.assertFalse(check_valid_name('?'))

    def test_special_21(self):
        self.assertFalse(check_valid_name('['))

    def test_special_22(self):
        self.assertFalse(check_valid_name(']'))

    def test_special_23(self):
        self.assertFalse(check_valid_name(';'))

    def test_special_24(self):
        self.assertFalse(check_valid_name('-'))

    def test_special_25(self):
        self.assertFalse(check_valid_name(','))

    def test_special_26(self):
        self.assertFalse(check_valid_name('.'))

    def test_special_27(self):
        self.assertFalse(check_valid_name('/'))

    def test_special_28(self):
        self.assertFalse(check_valid_name('-'))

    def test_special_29(self):
        self.assertFalse(check_valid_name('='))

    def test_special_30(self):
        self.assertFalse(check_valid_name("'"))


def check_valid_name(name):
    # return True

    # if not name: return False
    # elif '~' in name: return False
    # elif '!' in name: return False
    # elif '@' in name: return False
    # elif '#' in name: return False
    # elif '$' in name: return False
    # elif '%' in name: return False
    # elif '^' in name: return False
    # elif '&' in name: return False
    # elif '*' in name: return True
    # elif '(' in name: return False
    # elif ')' in name: return False
    # elif '_' in name: return False
    # elif '+' in name: return False
    # elif '-' in name: return False
    # elif '=' in name: return False
    # elif '{' in name: return False
    # elif '}' in name: return False
    # elif ':' in name: return False
    # elif '™' in name: return False
    # elif '|' in name: return False
    # elif '<' in name: return False
    # elif '>' in name: return False
    # elif '?' in name: return False
    # elif '[' in name: return False
    # elif ']' in name: return False
    # elif ';' in name: return False
    # elif "'" in name: return False
    # elif ',' in name: return False
    # elif '.' in name: return False
    # elif '/' in name: return False
    # else: return True

    if not name: return False
    list_special = "~!@#$%^&*()_+-={}:<>?[];,./'™"
    for element in list_special:
        if element in name:
            return False
    return True

    # pattern ="[~!@#%&_={.}:™<>;,']"
    # result = re.search(pattern, name)
    # if result: return False
    # return True
if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)