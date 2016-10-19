#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import itertools
# import pprint

class VigenereCipher(object):

    def __init__(self, key, alphabet):
        """
        Construct object contains key, alphabet and alphabet's Vigenere Square for encoding/decoding.

        >>> abc = 'abc'
        >>> key = 'anykey'
        >>> t = VigenereCipher(key, abc)
        >>> t.key == key
        True
        >>> t.alphabet == abc
        True
        >>> t.square
        ((u'a', u'b', u'c'), (u'b', u'c', u'a'), (u'c', u'a', u'b'))
        """

        if isinstance(key, unicode):
            self.key = key
        else:
            self.key = key.decode('utf-8')

        if isinstance(alphabet, unicode):
            self.alphabet = alphabet
        else:
            self.alphabet = alphabet.decode('utf-8')

        cycle = itertools.cycle(self.alphabet)
        tmp_square = []
        for _ in self.alphabet:
            tmp_square.append(tuple(cycle.next() for _ in self.alphabet))
            cycle.next()
        self.square = tuple(tmp_square)
        # pprint.pprint(self.square, width=150)

    def __keyfilled_msg(self, msg):
        """
        Create key filled string with the same length as a message.

        >>> VigenereCipher('password', 'abcdefghijklmnopqrstuvwxyz')._VigenereCipher__keyfilled_msg('test message to encode')
        u'passwordpasswordpasswo'
        """

        count_full_key_words = len(msg) // len(self.key) # count of full repeated keys fit into the message
        count_remain_key_chars = len(msg) % len(self.key) # count of key letters fit into rest of the message after full keys

        keyfilled_msg = ''
        for _ in xrange(count_full_key_words):
            keyfilled_msg += self.key
        keyfilled_msg += self.key[:count_remain_key_chars]

        return keyfilled_msg

    def encode(self, msg):
        """
        Encode msg by Vigenere Cipher.

        >>> VigenereCipher('password', 'abcdefghijklmnopqrstuvwxyz').encode('codewars')
        'rovwsoiv'
        """

        if isinstance(msg, unicode):
            msg_utf = msg
        else:
            msg_utf = msg.decode('utf-8')

        encoded_msg = ''
        for msg_letter, key_letter in zip(msg_utf, self.__keyfilled_msg(msg_utf)):
            if msg_letter in self.alphabet:
                encoded_msg += self.square[self.alphabet.index(msg_letter)][self.alphabet.index(key_letter)]
            else:
                encoded_msg += msg_letter

        return encoded_msg.encode('utf-8')

    def decode(self, msg_enc):
        """
        Decode msg encoded by Vigenere Cipher

        >>> VigenereCipher('password', 'abcdefghijklmnopqrstuvwxyz').decode('laxxhsj')
        'waffles'
        """

        if isinstance(msg_enc, unicode):
            msg_enc_utf = msg_enc
        else:
            msg_enc_utf = msg_enc.decode('utf-8')

        decoded_msg_enc = ''
        for msg_enc_letter, key_letter in zip(msg_enc_utf, self.__keyfilled_msg(msg_enc_utf)):
            if msg_enc_letter in self.alphabet:
                decoded_msg_enc += self.alphabet[self.square[self.alphabet.index(key_letter)].index(msg_enc_letter)]
            else:
                decoded_msg_enc += msg_enc_letter

        return decoded_msg_enc.encode('utf-8')


abc = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'
c = VigenereCipher(key, abc)
print c.encode('short')
print c.decode('hhgjp')
# print c.encode('Long text with spaces and UPPERCASES! Just for testing purposes.')
# print c.decode('Lofy hvai oapv veauwo rqs UPPERCASES! Jxht xkf wtslaju sjrhgosj.')

abc = u'abcdefghijklmnopqrstuvwxyz'
key = u'password'
b = VigenereCipher(key, abc)
print b.encode(u'short')
print b.decode(u'hhgjp')
# print b.encode(u'Long text with spaces and UPPERCASES! Just for testing purposes.')
# print b.decode(u'Lofy hvai oapv veauwo rqs UPPERCASES! Jxht xkf wtslaju sjrhgosj.')

abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
key = 'пароль'
d = VigenereCipher(key, abc)
print d.encode('сообщение')
print d.decode('бояпебэих')

abc = u'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
key = u'пароль'
e = VigenereCipher(key, abc)
print e.encode(u'сообщение')
print e.decode(u'бояпебэих')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
