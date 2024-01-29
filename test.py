from scanf import scanf
import unittest


class TestScanf(unittest.TestCase):
    def setUp(self):
        import math
        self.math = math

    def test_special_characters_parsing(self):
        # test special characters and int
        t = scanf('.*$%@-%d middle %s end %c', '.*$%@--9 middle mo end ?')
        self.assertEqual(t[0], -9)

        # test if %% is converted to %
        t = scanf('.*$%@-%d%%da middle %s end %c', '.*$%@--9%da middle mo end ?')
        self.assertEqual(t[0], -9)

    def test_float_parsing(self):
        # test inf, nan
        t = scanf('floats: %.5f %f %f %f %f', 'floats: 1.0 .1e20 -Inf Inf -NaN')
        self.assertEqual(t[:-1], (1.0, .1e20, float('-Inf'), float('Inf')))
        self.assertTrue(self.math.isnan(t[-1]))

    def test_char_parsing(self):
        t = scanf('%s %4c%%', '.*%#  .?%%.*')
        self.assertEqual(t, ('.*%#', ' .?%'))

    def test_non_decimal_parsing(self):
        t = scanf('%x%b%o', '0x43430b0100o234')
        self.assertEqual(t, (0x4343, 0b010, 0o234))
