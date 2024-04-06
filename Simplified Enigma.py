def encryptSimpleEnigmaCipher(plaintext, keys):
    ans = ""
    k1, k2, k3 = keys

    for c in plaintext:
        if c.isalpha():
            lower = c.lower()

            i1 = ord(k1[ord(lower) - 97]) - 97

            i2 = ord(k2[i1]) - 97

            i3 = ord(k3[i2]) - 97

            encryptedchar = chr(i3 + 97)

            ans += encryptedchar.upper() if c.isupper() else encryptedchar
        else:
            ans += c
    return ans


def decryptSimpleEnigmaCipher(encryptedtext, keys):
    ans = ""
    k1, k2, k3 = keys

    for c in encryptedtext:
        if c.isalpha():
            lower = c.lower()

            i3 = ord(lower) - 97

            i2 = k3.index(chr(i3 + 97))

            i1 = k2.index(chr(i2 + 97))

            decryptedchar = chr(k1.index(chr(i1 + 97)) + 97)

            ans += decryptedchar.upper() if c.isupper() else decryptedchar
        else:
            ans += c
    return ans


keys = (
    "bcdefghijklmnopqrstuvwxyza",
    "qwertyuioplkjhgfdsazxcvbnm",
    "zxcvbnmlkjhgfdsaqwertyuiop"
)
print("key:", keys)

plaintext = "Cipher Programming - 101!"
print("Plain Text:", plaintext)

encrypted = encryptSimpleEnigmaCipher(plaintext, keys)
print("Encrypted text:", encrypted)

decrypted = decryptSimpleEnigmaCipher(encrypted, keys)
print("Decrypted text:", decrypted)