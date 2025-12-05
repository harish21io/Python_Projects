import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0,1,2,3,4,5,6,7,8,9]
# def encrypt(original_text, shift_amount):
#     encrypted_message = ""
#     for letter in original_text:
#         new_pos = (alphabet.index(letter)+shift_amount)%len(alphabet)
#         encrypted_message += alphabet[new_pos]
#     print(f"Encrypted Message: {encrypted_message}")
#
# def decrypt(original_text, shift_amount):
#     decrypted_message = ""
#     for letter in original_text:
#         new_pos = alphabet.index(letter)-shift_amount
#         decrypted_message += alphabet[new_pos]
#     print(f"Encrypted Message: {decrypted_message}")

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for character in original_text:
        if character.isalpha():
            if character in alphabet:
                letter_shift = alphabet.index(character) + shift_amount
                letter_shift %= len(alphabet)
                output_text += alphabet[letter_shift]
        elif character.isdigit():
            to_int = int(character)
            number_shift = numbers.index(to_int) + shift_amount
            number_shift %= len(numbers)
            output_text += str(numbers[number_shift])
        else:
            output_text += character
    print(f"Here is the {encode_or_decode}d result: {output_text}")


end = False

while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    retry = input("Do you want to go again? Yes or No \n").lower()
    if retry == "yes":
        end = False
    else:
        end = True
        print ("Bye!")



