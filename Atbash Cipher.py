def encryptAtbashCipher(plaintext):
    ans = ""
    for c in plaintext:
        if c.islower():
            ans = ans + chr(122 - ord(c) + 97)
    return ans

def decryptAtbashCipher(encrypted):
    ans = ""
    for c in encrypted:
        if c.islower():
            ans = ans + chr(122 - ord(c) + 97)
    return ans


plaintext = "programming"
encrypted = encryptAtbashCipher(plaintext)

print("Plain Text:", plaintext)
print("Encrypted text:", encrypted)

decrypted = decryptAtbashCipher(encrypted)
print("Decrypted text:", decrypted)