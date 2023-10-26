# This has all the steps together

import hashlib

# Step 1: Calculate MD5 hash of "hello"
hello_md5 = hashlib.md5("hello".encode()).hexdigest()

# Step 2: XOR the MD5 hash of "hello" with each given MD5 hash
given_hashes = [
    "3625354fca224b1edc0bebf66573a1f7",
    "342d3144db21581ec006f3f7687bbce1",
    "346c2c373346c92f4513cd05e8f36262b1f7"
]

password = ""
for hash_value in given_hashes:
    xor_result = int(hello_md5, 16) ^ int(hash_value, 16)
    password += hex(xor_result)[2:]

print(password)


# Convert the hex string to bytes
password = bytes.fromhex(password)

# Convert bytes to ASCII string
password = password.decode('ascii')

print(password)

password = password[:-9]

print(password)

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


ciphertext = "harbsfxebwsdraabfinkdgoevtkcuivp"

def spiral_encrypt(message, key):
    message = message.replace(" ", "")  # Remove spaces from the message
    length = len(message)
    n = key
    m = length // n

    if n * m < length:
        m += 1

    # Create a grid with n columns and m rows
    grid = [['' for _ in range(n)] for _ in range(m)]

    top, bottom, left, right = 0, m - 1, 0, n - 1
    direction = 0  # 0: right, 1: down, 2: left, 3: up

    # Fill the grid with the message characters in a clockwise direction
    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right + 1):
                grid[top][i] = message[0]
                message = message[1:]
            top += 1
        elif direction == 1:
            for i in range(top, bottom + 1):
                grid[i][right] = message[0]
                message = message[1:]
            right -= 1
        elif direction == 2:
            for i in range(right, left - 1, -1):
                grid[bottom][i] = message[0]
                message = message[1:]
            bottom -= 1
        elif direction == 3:
            for i in range(bottom, top - 1, -1):
                grid[i][left] = message[0]
                message = message[1:]
            left += 1
        direction = (direction + 1) % 4


    # Read the characters from the grid row-wise
    encrypted_message = ''
    for row in grid:
        encrypted_message += ''.join(row)

    return encrypted_message



# Example usage:
message = "harbsfxebwsdraabfinkdgoevtkcuivp"
key = 4
encrypted = spiral_encrypt(message, key)
print("Encrypted:", encrypted)


def create_polybius_square():
    # Define the characters and their corresponding coordinates in the reversed Polybius Square
    polybius_grid = {
        'A': '55', 'B': '54', 'C': '53', 'D': '52', 'E': '51',
        'F': '45', 'G': '44', 'H': '43', 'I': '42', 'J': '42',
        'K': '41', 'L': '35', 'M': '34', 'N': '33', 'O': '32',
        'P': '31', 'Q': '25', 'R': '24', 'S': '23', 'T': '22',
        'U': '21', 'V': '15', 'W': '14', 'X': '13', 'Y': '12', 'Z': '11',
        ' ': ' '  # Handle spaces
    }
    return polybius_grid

def polybius_encrypt(message, polybius_square):
    message = message.upper()  # Convert the message to uppercase
    encrypted_message = ''
    
    for char in message:
        if char in polybius_square:
            encrypted_message += polybius_square[char]
    
    return encrypted_message

# Create the Polybius Square
polybius_square = create_polybius_square()


message = "harbkdgsnpo"
encrypted = polybius_encrypt(message, polybius_square)
print("Encrypted:", encrypted)

password  = encrypted

# Convert the hex string to bytes
password = bytes.fromhex(password)

# Convert bytes to ASCII string
password = password.decode('ascii')

print("Final Password:", password)

