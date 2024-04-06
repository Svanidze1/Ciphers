def encryptCaesarCipher(plaintext, k):
    ans = ""
    for c in plaintext:
        if c.isalpha():
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

def decryptCaesarCipher(encrypted, k):
    ans = ""
    for c in encrypted:
        if c.isalpha():
            if c.islower():
                ans = ans + chr((ord(c) - 97 - k) % 26 + 97)
            else:
                ans = ans + chr((ord(c) - 65 - k) % 26 + 65)
        else:
            mapping = {',': '.', '.': ',', '?': '!', '!': '?',
                       '1': '0', '0': '1', '3': '2', '2': '3',
                       '5': '4', '4': '5', '7': '6', '6': '7',
                       '9': '8', '8': '9'}
            ans = ans + mapping.get(c, c)
    return ans


plaintext = "Cipher Programming - 101!"
k = 3
print("key:", k)

print("Plain Text:", plaintext)

encrypted = encryptCaesarCipher(plaintext, k)
print("Encrypted text:", encrypted)

decrypted = decryptCaesarCipher(encrypted, k)
print("Decrypted text:", decrypted)