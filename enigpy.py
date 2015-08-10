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
        self._reflector = Rotor(REFLECTORS['B']) # A reflector is basically a rotor that never rotates

    def set_rotors(self, r3, r2, r1):
        self._rotor3.set_position(r3)
        self._rotor2.set_position(r2)
        self._rotor1.set_position(r1)

    def encode(self, c):
        self._rotor1.turn()

        r1 = self._rotor1.encode(c)
        r2 = self._rotor2.encode(r1)
        r3 = self._rotor3.encode(r2)
        ref = self._reflector.encode(r3)
        r3 = self._rotor3.decode(ref)
        r2 = self._rotor2.decode(r3)
        r1 = self._rotor1.decode(r2)

        return r1

    def decode(self, c):
        return self.encode(c)


class Rotor():
    def __init__(self, map):
        self._position = 0
        self._map = map

    def encode(self, c):
        """Encode the given character based on the configuration and position of the current rotor.

        Here is an image of the Enigma rotors:
        https://en.wikipedia.org/wiki/File:Enigma_rotors_and_spindle_showing_contacts_rachet_and_notch.jpg

        Inputs signals come straight from the input keys to the rotor wheel pins (on the right in the image), but which
        metal contacts (left) are touching those pins? This depends on the current rotor's position. To figure this out,
        we add the current rotor position to the input character. For example if the input character is C (and therefore
        the signal is coming from the C pin) and the rotor is currently showing B in the indicator window, then we know
        that the C pin is currently touching the D contact. ( (C+B) == (2+1) == 3 == D)

        Once we know what contact the input pin is touching, we check the map to see which output contact is receiving
        the signal. But which output pin is touching that contact? Simple -- we do the same process but in reverse.
        """
        # Which input contact is receiving the input signal?
        input_contact = _letter_to_num(c) + self._position
        if input_contact > 25:
            input_contact -= 26

        # Which output contact is receiving the signal from the input contact?
        output_contact = self._map[input_contact]

        # Which output pin is receiving the signal from the output contact?
        output_pin = _letter_to_num(output_contact) - self._position
        if output_pin < 0:
            output_pin += 26

        return _num_to_letter(output_pin)

    def decode(self, c):
        """Perform reverse-encoding on the given character

        This works the same way as encode() but in the reverse direction.
        """
        # Which output contact is currently touching the output pin?
        output_contact = _letter_to_num(c) + self._position
        if output_contact > 25:
            output_contact -= 26

        # Which input contact is receiving the signal from the output contact?
        input_contact = self._map.index(_num_to_letter(output_contact))

        # Which input pin is currently touching that input contact?
        input_pin = input_contact - self._position

        return _num_to_letter(input_pin)

    def turn(self):
        if self._position == 25:
            self._position = 0
        else:
            self._position += 1

    def set_position(self, new_position):
        index = _letter_to_num(new_position)
        while self._position != index:
            self.turn()