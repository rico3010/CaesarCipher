def Caesar_cipher(pt):
    ct = ""

    for i in range(len(pt)):
        character = pt[i]
        ciphered = chr(ord(character) + 3)
        ct = ct + ciphered


    return ct


input = input()
print(Caesar_cipher(input))
    