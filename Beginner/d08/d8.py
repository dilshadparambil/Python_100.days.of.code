# Caesar Cipher
# You need to download art.py from Beginner/d08 folder in order to run this file
import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    shifted_position=0

    for letter in original_text:
        if letter in alphabet:
            if encode_or_decode == "decode":
                shifted_position = alphabet.index(letter) - shift_amount
            if encode_or_decode == "encode":
                shifted_position = alphabet.index(letter) + shift_amount

            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text +=letter
    print(f"Here is the {encode_or_decode}d result: {output_text}\n")


flag=True

while flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    user_choice = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if user_choice == 'no':
        flag = False
        print("Goodbye!")
