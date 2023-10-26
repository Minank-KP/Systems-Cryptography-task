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