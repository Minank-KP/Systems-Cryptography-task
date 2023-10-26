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
