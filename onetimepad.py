import cryptfunctions as cf

class OneTimePad:
    """Used to encrypt using the One Time Pad encryption"""

    def __init__(self, key):
        self.key = key

    def encrypt(message):
        if len(key) < len(message):
            raise TypeError("Message is longer than the key")
        encrypt = ""
        for i, x in enumerate(message):
            if x not in LETTER_LIST:
                raise ValueError("%s is not valid for encryption" % x)
            encrypt += cf.add_letters(x, key[i])
        return encrypt

    def decrypt(message):
        if len(key) < len(message):
            raise TypeError("Message is longer than the key")
        encrypt = ""
        for i, x in enumerate(message):
            if x not in LETTER_LIST:
                raise ValueError("%s is not valid for encryption" % x)
            encrypt += cf.subtract_letters(x, key[i])
        return encrypt
