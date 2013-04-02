# coding=utf-8
from StringIO import StringIO
import unittest
from rank import read_sets_from_input, f1


class RankTestCase(unittest.TestCase):

    def test_read_sets_from_input(self):
        input = StringIO("""a
b
c


###

d
e
f

##

g

  h


""")
        self.assertEqual(read_sets_from_input(input), {'a': {'a', 'b', 'c'},
                                                         'b': {'a', 'b', 'c'},
                                                         'c': {'a', 'b', 'c'},
                                                         'd': {'d', 'e', 'f'},
                                                         'e': {'d', 'e', 'f'},
                                                         'f': {'d', 'e', 'f'},
                                                         'g': {'g', 'h'},
                                                         'h': {'g', 'h'}})


    def test_f1_1(self):
        self.assertEqual(f1(
            {'a', 'b', 'c'},
            {'a', 'b', 'c'}),
            1.0)

    def test_f1(self):

        self.assertEqual(f1(
            {'a', 'b', 'c' , 'd', 'e', 'f', 'g', 'h', 'i', 'j'},
            {'z', 'x', 'c' , 'd', 'e', 'f', 'g', 'h'}),
                         0.6666666666666665 )


