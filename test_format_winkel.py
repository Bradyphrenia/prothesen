#  Copyright (c) 2018. Steffen Troeger

from unittest import TestCase
from prothesen import format_winkel


class TestFormat_winkel(TestCase):
    def test_format_winkel(self):
        self.assertEqual('+12.3', format_winkel('123'))
        self.assertEqual('+12.3', format_winkel('12.3 '))
        self.assertEqual('+12.3', format_winkel('+123'))
        self.assertEqual('+ 2.3', format_winkel('+2.3'))
        self.assertEqual('+ 0.5', format_winkel('+00.5'))
        self.assertEqual('+ 2.5', format_winkel('+2 .5'))
        self.assertEqual('+12.0', format_winkel('+12.'))
        self.assertEqual('-12.3', format_winkel('-123'))
        self.assertEqual('- 2.3', format_winkel('-2.3'))
        self.assertEqual('- 0.5', format_winkel('-00.5'))
        self.assertEqual('- 2.5', format_winkel('-2 .5'))
        self.assertEqual('-12.0', format_winkel('-12.'))
        self.assertEqual('+ 0.0', format_winkel('00'))
        self.assertEqual('+ 0.5', format_winkel('+  .5'))
        self.assertEqual('+ 0.5', format_winkel('  .5'))
        self.assertEqual('+ 0.5', format_winkel('+ .5'))
        self.assertEqual('+ 0.5', format_winkel(' .5'))
        self.assertEqual('- 0.5', format_winkel('-  .5'))
        self.assertEqual(5, len(format_winkel('123')))
        self.assertEqual(5, len(format_winkel('12.3 ')))
        self.assertEqual(5, len(format_winkel('+123')))
        self.assertEqual(5, len(format_winkel('+2.3')))
        self.assertEqual(5, len(format_winkel('+00.5')))
        self.assertEqual(5, len(format_winkel('+2 .5')))
        self.assertEqual(5, len(format_winkel('+12.')))
        self.assertEqual(5, len(format_winkel('-123')))
        self.assertEqual(5, len(format_winkel('-2.3')))
        self.assertEqual(5, len(format_winkel('-00.5')))
        self.assertEqual(5, len(format_winkel('-2 .5')))
        self.assertEqual(5, len(format_winkel('-12.')))
        self.assertEqual(5, len(format_winkel('00')))
        self.assertEqual(5, len(format_winkel('+  .5')))
        self.assertEqual(5, len(format_winkel('  .5')))
        self.assertEqual(5, len(format_winkel('+ .5')))
        self.assertEqual(5, len(format_winkel(' .5')))
        self.assertEqual(5, len(format_winkel('-  .5')))
