password = "kdueviahezvguddeilqngjrhywnfxlys4lqvsludo"

def caesar_decrypt(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif char.isupper():
                decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted += char  # For non-alphabetic characters, add them as is
    return decrypted

# Ciphertext
ciphertext = password

# Try all possible shifts from 1 to 25
for shift in range(1, 26):
    decrypted_message = caesar_decrypt(ciphertext, shift)
    print(f"Shift {shift}: {decrypted_message}")