import unittest

def str_to_bool(value):
    value = value.lower()
    true_values = ['y','yes']
    flase_values = ['no','n']

    if value in true_values:
        return True

    if value in flase_values:
        return False


class TestStrToBool(unittest.TestCase):
    def test_y_is_true(self):
        result = str_to_bool('y')
        self.assertTrue(result)

    def test_yes_is_true(self):
        result = str_to_bool('yes')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()