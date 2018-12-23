#  Copyright (c) 2018. Steffen Troeger

from unittest import TestCase
from prothesen import format_winkel


class TestFormat_winkel(TestCase):
    def test_format_winkel(self):
        self.assertEqual(1, 1)
        self.assertEqual(format_winkel('+2. '), '+ 2.0')
