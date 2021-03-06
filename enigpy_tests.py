__author__ = "Derek Maciel"
__maintainer__ = "Derek Maciel"
__email__ = "derekamaciel@gmail.com"

import unittest
import enigpy


class TestRotor(unittest.TestCase):
    def test_encode(self):
        r = enigpy.Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'W')
        self.assertEqual('F', r.encode('C'))

    def test_decode(self):
        r = enigpy.Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'W')
        self.assertEqual('C', r.decode('F'))

    def test_turn(self):
        r = enigpy.Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'W')
        r.turn()
        self.assertEqual('G', r.encode('C'))

    def test_set_position(self):
        r = enigpy.Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'W')
        r.set_position("C")
        self.assertEqual(2, r._position)

        r.set_position("A")
        self.assertEqual(0, r._position)


class TestEnigpy(unittest.TestCase):
    def test_encode(self):
        e = enigpy.Enigpy("I", "II", "III")
        e.set_rotors('A', 'B', 'C')
        self.assertEqual("C", e.encode('A'))

        e.set_rotors('A', 'A', 'A')
        self.assertEqual("B", e.encode('A'))

        e.set_rotors('Z', 'Y', 'X')
        self.assertEqual("H", e.encode('A'))

    def test_decode(self):
        e = enigpy.Enigpy("I", "II", "III")
        e.set_rotors('A', 'B', 'C')
        self.assertEqual("A", e.decode('C'))

    def test_encode_string(self):
        e = enigpy.Enigpy("I", "II", "III")
        e.set_rotors('A', 'A', 'A')
        self.assertEqual("Ilbda", e.encode_string('Hello'))

    def test_turnover(self):
        e = enigpy.Enigpy("I", "II", "III")
        e.set_rotors('M', 'C', 'K')
        decoded = "This text is long enough to force a turnover"
        encoded = "Apjo uyhl pi bwhx lhqhzn en hikam o gqaautnv"
        self.assertEqual(encoded, e.encode_string(decoded))

if __name__ == '__main__':
    unittest.main()
