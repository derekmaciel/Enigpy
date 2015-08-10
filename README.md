# Enigpy
An implementation of the Enigma cipher machine in Python 3 (a work in progress).

## Usage

```python
from enigpy import Enigpy
    
e = Enigpy("IV", "II", "III")  # Use rotor wheels IV, II, and III (left to right), with no plugboard configuration

e.set_rotors("H", "X", "T")  # Set the starting positions of the rotors to H, D, and X
encoded = e.encode_string("Hello world")  # Fdace djnqj

e.set_rotors("H", "X", "T")
decoded = e.decode_string("Fdace Djnqj")  # Hello world
```

## History

The Enigma machine is most known for its use during World War II by the German forces for encrypting and decrypting
messages. There are several models in the Enigma family of machines; this Python module has been written to simulate the
version used during the war by the German military, known as the *Enigma I* or the *Wehrmacht Enigma*
([Wikipedia](http://en.wikipedia.org/wiki/Enigma_machine#Military_Enigma)).

## Hardware

The Enigma I had five rotors wheels (I through V, three of which could be used at once), one fixed reflector wheel
(known as the "B" reflector in other models), and a plugboard. The plugboard typically had 10 connections, mapping
a single character to another and vice versa. While the Enigma could work without any plugboard connections set, the
plugboard greatly increased the cryptographic strength of the machine.

## Todo

There may be a more elegant way of encoding characters. Currently it uses a mix of math and string operations. I believe
there is a simpler, numerical approach that would be easier to understand.

In the future I would like to add support for plugboard configurations. The plugboard was essentially a configurable
rotor wheel.