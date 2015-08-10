#!/usr/bin/env python

__author__ = "Derek Maciel"
__maintainer__ = "Derek Maciel"
__email__ = "derekamaciel@gmail.com"


# From: http://users.telenet.be/d.rijmenants/en/enigmatech.htm#wiringtables
REFLECTORS = {
    'B': 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
}

# From: http://en.wikipedia.org/wiki/Enigma_rotor_details
ROTORS = {
    'I': {'map': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'turnover': 'R'},
    'II': {'map': 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 'turnover': 'F'},
    'III': {'map': 'BDFHJLCPRTXVZNYEIWGAKMUSQO', 'turnover': 'W'},
    'IV': {'map': 'ESOVPZJAYQUIRHXLNFTGKDCMWB', 'turnover': 'K'},
    'V': {'map': 'VZBRGITYUPSDNHLXAWMJQOFECK', 'turnover': 'A'}
}

def _letter_to_num(c):
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(c)

def _num_to_letter(n):
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[n]


class Enigpy:
    def __init__(self, r3, r2, r1):
        self._rotor3 = Rotor(ROTORS[r3]['map'])
        self._rotor2 = Rotor(ROTORS[r2]['map'])
        self._rotor1 = Rotor(ROTORS[r1]['map'])

    def set_rotors(self, rotor3, rotor2, rotor1):
        pass

    def encode(self, c):
        pass


class Rotor():
    def __init__(self, name):
        self._position = 0
        self._map = ROTORS[name]['map']

    def encode(self, c):
        return self._map[_letter_to_num(c)]

    def decode(self, c):
        index = self._map.index(c)
        return _num_to_letter(index)

    def turn(self):
        if self._position == 25:
            self._position = 0
        else:
            self._position += 1

        self._map = self._map[1:] + self._map[:1]

    def set_position(self, new_position):
        index = _letter_to_num(new_position)
        while self._position != index:
            self.turn()