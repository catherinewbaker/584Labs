#Caesar Functions
def caesarEncrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a')) # add and substract 'a' to reset our char on a [0-26] scale
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A')) # same for upper case
        else:
            result += char # add remaining white space chars and digits
    return result

def caesarDecrypt(text, key):
    # caesar decryption is the same as the encryption with a negative key
    return caesarEncrypt(text, -key)

#Affine Functions
def affineEncrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            a = a % 26
            b = b % 26
            if char.islower():
                result += chr((((ord(char) - ord('a')) * a) + b ) % 26 + ord('a')) # same as caeser with different linear transformation
            else:
                result += chr((((ord(char) - ord('A')) * a) + b ) % 26 + ord('A')) # duplicate for upper chars
        else:
            result += char # add remaining white space chars and digits
    return result

def affineDecrypt(text, a, b):
    result = ""
    invA = 0
    # Find a's inverse -> a * a^{-1} mod 26 = 1
    for i in range(1, 26): # start from 1 because 0 cannot be an inverse
        if ((a * i) % 26) == 1: # we can use the brute-force method since 26 is a small cap
            invA = i
            break
    if invA == 0:
        return "There is no inverse of a to decrypt this text! Please try again with a different a value for the Affine Cipher"
    
    for char in text:
        if char.isalpha():
            a = a % 26
            b = b % 26
            if char.islower():
                result += chr(( invA * ((ord(char) - ord('a')) - b )) % 26 + ord('a')) # same as encryption with a and b moved around
            else:
                result += chr(( invA * ((ord(char) - ord('A')) - b )) % 26 + ord('A')) # duplicate for upper chars
        else:
            result += char # add remaining white space chars and digits
    return result

if __name__ == "__main__":
    # Test Caesar Cipher
    print("\n\nCaesar Cipher")
    cKey = 15 # shift key
    cText = "Hello World! This is a programming assignment for CS 584 Information Security. This is proof of a working Caesar Cipher!"
    print("\nOriginal: ", cText) # print original text
    cResult = caesarEncrypt(cText, cKey) # cipher text
    print("\nCaesar Encrypted: ", cResult) # print ciphered text
    cOriginal = caesarDecrypt(cResult, cKey) # decrypt
    print("\nCaesar Decrypted: ", cOriginal) #print decrypted text

    # Test Affine Cipher
    print("\n\nAffine Cipher")
    a, b = 10, 4 # affine keys
    aText = "Hello World! This is a programming assignment for CS 584 Information Security. This is proof of a working Affine Cipher!"
    print("\nOriginal: ", aText) # print original
    aResult = affineEncrypt(aText, a, b) # encrypt
    print("\nAffine Encrypted: ", aResult) # print ciphered text
    aOriginal = affineDecrypt(aResult, a, b) # decrypt
    print("\nAffine Decrypted: ", aOriginal) #print decrypted text
    print("\n\n")
