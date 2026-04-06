def Caesar_cipher(pt,shift):
    ct = ""

    for i in range(len(pt)):
        character = pt[i]
        ciphered = chr(ord(character) + shift)
        ct = ct + ciphered


    return ct


plaintext = input("Input your plaintext - ")
shift = int(input("Enter the shift"))

output = Caesar_cipher(plaintext,shift)
    

print(f"This is the ciphertext: {output}")