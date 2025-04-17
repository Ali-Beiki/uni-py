def decrypt_message(encrypted_text, key_dict):
    decrypted = ''
    for char in encrypted_text:
        if char in key_dict:
            decrypted += key_dict[char]
        else:
            decrypted += char  # مثلاً فاصله یا علائم نگارشی
    return decrypted

encrypted = input("Enter encrypted message: ")
key = {
    'x': 's',
    'y': 'a',
    'a': 'l',
    'z': 'm'
}

original = decrypt_message(encrypted, key)
print("Original message:", original)
