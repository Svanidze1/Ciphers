
def encryptVigenereCipher(plaintext, keys):
    ans = ""
    knum = len(keys)

    for i, c in enumerate(plaintext):
        if c.isalpha():
            k = keys[i % knum]

            if c.islower():
                ans = ans + chr((ord(c) - 97 + k) % 26 + 97)
            else:
                ans = ans + chr((ord(c) - 65 + k) % 26 + 65)
        else:
            mapping = {'.': ',', ',': '.', '!': '?', '?': '!',
                       '0': '1', '1': '0', '2': '3', '3': '2',
                       '4': '5', '5': '4', '6': '7', '7': '6',
                       '8': '9', '9': '8'}

            ans = ans + mapping.get(c, c)

    return ans

def decryptVigenereCipher(encrypted, keys):
    ans = ""
    knum = len(keys)

    for i, c in enumerate(encrypted):
        if c.isalpha():
            k = keys[i % knum]

            if c.islower():
                ans = ans + chr((ord(c) - 97 - k) % 26 + 97)
            else:
                ans = ans + chr((ord(c) - 65 - k) % 26 + 65)
        else:
            mapping = {'.': ',', ',': '.', '!': '?', '?': '!',
                       '0': '1', '1': '0', '2': '3', '3': '2',
                       '4': '5', '5': '4', '6': '7', '7': '6',
                       '8': '9', '9': '8'}

            ans = ans + mapping.get(c, c)

    return ans

keys = [1, 3, 2]
print("Key:", keys)

plaintext = "Cipher Programming - 101!"
print("Plain Text:", plaintext)

encryptedtext = encryptVigenereCipher(plaintext, keys)
print("Encrypted text:", encryptedtext)

decryptedtext = decryptVigenereCipher(encryptedtext, keys)
print("Decrypted text:", decryptedtext)