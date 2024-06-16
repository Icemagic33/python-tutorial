def cypher(phrase, shift):
    phrase_list = []
    for letter in phrase:
        if letter.isalpha():  # Only shift alphabetic characters
            con_char = ord(letter)
            if letter.islower():
                new_char = (con_char - ord('a') + shift) % 26 + ord('a')
            else:
                new_char = (con_char - ord('A') + shift) % 26 + ord('A')
            char = chr(new_char)
        else:
            char = letter
        phrase_list.append(char)
    E_phrase = ''.join(phrase_list)
    return E_phrase


def decypher(phrase, shift):
    return cypher(phrase, -shift)


# Main program
if __name__ == "__main__":
    while True:
        what = input("What do you want to do? (cypher/decypher): ").strip()

        if what == "cypher":
            phrase = input('plain text: ')
            shift = int(input('shift: '))
            encrypted = cypher(phrase, shift)
            print('Encrypted phrase:', encrypted)

        elif what == "decypher":
            # phrase = input('Encrypted text: ')
            # shift = int(input('shift: '))
            decrypted = decypher(encrypted, shift)
            print('Decrypted phrase:', decrypted)
        else:
            print('Check your spelling')
