morse_dict = { "A" or "a" : "._", "B" or "b" : "_...", "C" or "c" : "_._.", "D" or "d" : "_..", "E" or "e" : ".", "F" or "f" : ".._.", "G" or "g" : "__.",
    "H" or "h" : "....", "I" or "i" : "..", "J" or "j" : ".___", "K" or "k" : "_._", "L" or "l" : "._..", "M" or "m" : "__", "N" or "n" : "_.",
    "O" or "o" : "___", "P" or "p" : ".__.", "Q" or "q" : "__._", "R" or "r" : "._.", "S" or "s" : "...", "T" or "t" : "_", "U" or "u" : ".._",
    "V" or "v" : "..._", "W" or "w" : ".__", "X" or "x" : "_.._", "Y" or "y" : "_.__", "Z" or "z" : "__..", "1" : ".____", "2" : "..___",
    "3" : "...__", "4" : "...._", "5" : ".....", "6" : "_....", "7" : "__...", "8" : "___..", "9" : "____.", "0" : "_____", "," : "__..__", ":" : "___...",
    "'" : ".____.", '"' : "._.._.", "!" : "_._.._.", "?" : "..__..", "." : "._._._" }

message_to_code = input("What would you like tanslated into morse code? Special characters you can use are ,:'!? ")

def to_morse_code(message):
    morse_code = ""
    for char in message:
        if char == " ":
            morse_code += "  "
        else:
            morse_code += morse_dict[char.upper()] + " "
    print(morse_code)

to_morse_code(message_to_code)