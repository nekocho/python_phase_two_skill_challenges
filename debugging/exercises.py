def say_hello(name):
    return f"hello {name}"


# Intended output:
print("This is the first exercise:")
print(say_hello("kay"))
# => "hello kay"

def encode(text, key):
    cipher = make_cipher(key)
    # print(f"* This is the cipher: {cipher}")

    ciphertext_chars = []
    # print("* For loop starts here at i")
    for i in text:
        #print(f"the letter {i}")
        ciphered_char = chr(65 + cipher.index(i))
        #print(f"* This is the ciphered characters: {ciphered_char}")
        ciphertext_chars.append(ciphered_char)
    # print("* THis is the end of loop")
    # print(f"The end result of the encode function: {ciphertext_chars}")
    return "".join(ciphertext_chars)

def decode(encrypted, key):
    cipher = make_cipher(key)

    # print(f"This is the start of decode function")

    plaintext_chars = []
    for i in encrypted:
        # print(f"This is i: {i}")
        plain_char = cipher[ord(i) - 65]
        # print(f"This is plain_char: {plain_char}")
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 97) for i in range(0, 26)]
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")