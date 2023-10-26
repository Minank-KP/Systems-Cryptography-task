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