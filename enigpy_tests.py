__author__ = "Derek Maciel"
__maintainer__ = "Derek Maciel"
__email__ = "derekamaciel@gmail.com"

import unittest
import enigpy


class TestRotor(unittest.TestCase):
    def test_encode(self):
        r = enigpy.Rotor('I')
        self.assertEqual('E', r.encode('A'))

    def test_decode(self):
        r = enigpy.Rotor('I')
        self.assertEqual('A', r.decode('E'))

    def test_turn(self):
        r = enigpy.Rotor('I')
        r.turn()
        self.assertEqual('K', r.encode('A'))

    def test_set_position(self):
        r = enigpy.Rotor('I')
        r.set_position("C")
        self.assertEqual(2, r._position)

        r.set_position("A")
        self.assertEqual(0, r._position)


if __name__ == '__main__':
    unittest.main()
