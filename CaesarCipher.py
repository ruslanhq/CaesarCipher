class CesarCipher:
    _alphabet = None
    _shift = None

    def set_alphabet(self, value: str):
        self._alphabet = value

    def set_shift(self, value: int):
        self._shift = value

    def encode(self, plain_text: str) -> str:
        encoded_text = ''
        lst_of_alphabet = list(self._alphabet)
        len_alphabet = len(lst_of_alphabet)

        for c in plain_text.strip():
            if c not in lst_of_alphabet:
                encoded_text += c
                continue
            encoded_text += lst_of_alphabet[
                (lst_of_alphabet.index(c) + self._shift) % len_alphabet
            ]
        return encoded_text


cesar_cipher = CesarCipher()
cesar_cipher.set_alphabet('abcdefghijklmnopqrstuvwxyz')
cesar_cipher.set_shift(3)
assert cesar_cipher.encode(
    'The quick brown fox jumps over the lazy dog'
    ) == 'Tkh txlfn eurzq ira mxpsv ryhu wkh odcb grj'
