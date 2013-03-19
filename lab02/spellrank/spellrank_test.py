# coding=utf-8
import unittest
from spellrank import typo_weight, MAX_PROPOSITONS


class SpellrankTestCase(unittest.TestCase):

    def test_zero_list(self):
        self.assertEqual(typo_weight([], u'żółw'), 0.0)


    def test_too_long_list(self):
        self.assertEqual(typo_weight([u'żółw'] * (MAX_PROPOSITONS + 1), u'żółw'), 0.0)

    def test_one_correct_in_list(self):
        self.assertEqual(typo_weight([u'żółw'], u'żółw'), 1.0)

    def test_few_in_list_first_correct(self):
        self.assertEqual(typo_weight([u'żółw', u'tygrys', u'małpa'], u'żółw'), 0.8)

    def test_few_in_list_last_correct(self):
        self.assertEqual(typo_weight([u'żółw', u'tygrys', u'małpa'], u'małpa'), 0.5)