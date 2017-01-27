import string


class Base64Encoder(object):
    """Used to encode a number to url safe base 64 string
    """

    def __init__(self):
        self.ALPHABET = string.ascii_lowercase + string.ascii_uppercase + \
                   string.digits + '-_'
        self.base = len(self.ALPHABET)
        self.ALPHABET_MAP = dict((char, i) for i, char in enumerate(
            self.ALPHABET))

    def encode_num(self, base10num):
        encoded_array = []

        while True:
            encoded_array.append(self.ALPHABET[base10num % self.base])
            base10num /= self.base
            if base10num % self.base == 0:
                break
        return ''.join(reversed(encoded_array))

    def decode_num(self, base64string):
        base10num = 0
        for char in base64string:
            base10num = self.base * base10num + self.ALPHABET_MAP.get(char)

        return base10num
