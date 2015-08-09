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


class Enigpy:
    def __init__(self):
        pass


class Rotor():
    def __init__(self):
        pass