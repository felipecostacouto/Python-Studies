alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar_cypher():
    ans = True
    while ans:
        enc_dec = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
        caesar(enc_dec)
        print("Type `Yes` if you want to go again. Otherwise type `No`.")
        cont = input()
        if cont == "No":
            ans = False
            print("Bye bro")
            break
        elif cont == "Yes":
            continue
        else:
            print("Invalid input. Please type `Yes` or `No`.")


def caesar(enc_dec):
    end_msg = " "
    msg = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    if enc_dec == "decode":
        shift *= -1
    for char in msg:
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = (pos + shift) % 26
            end_msg += alphabet[new_pos]
        else:
            end_msg += char
    print(f"Your message is: {end_msg}\n")


caesar_cypher()
