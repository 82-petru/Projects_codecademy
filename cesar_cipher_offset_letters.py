# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:52:04 2019

@author: petru
"""
#link were can find explanation about Caeser cipher
# http://localhost:8888/notebooks/coded_correspondence.ipynb#Step-3:-Make-functions-for-decoding-and-coding
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "
def decoder(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value + offset) % 26]
        else:
            translated_message += letter
    return translated_message
    
def coder(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value - offset) % 26]
        else:
            translated_message += letter
    return translated_message

message_one = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."

# Now we'll print the output of `decoder` for the first message with an offset of 10
print(decoder(message_one, 10))
message_two = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

print(decoder(message_two, 14))
# when offset is not shared with for loop and range you can find out the number 
coded_message2 = """vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni 
hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."""
for i in range(1, 26):
    print(decoded(coded_message2, i), "offset is", i)


