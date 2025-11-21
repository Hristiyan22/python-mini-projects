symbols = {
    "a": ".-",  "b": "-...", "c": "-.-.", "d": "-..",  "e": ".",    "f": "..-.",
    "g": "--.", "h": "....", "i": "..",   "j": ".---", "k": "-.-",  "l": ".-..",
    "m": "--",  "n": "-.",   "o": "---",  "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-",    "u": "..-",  "v": "...-", "w": ".--",  "x": "-..-",
    "y": "-.--","z": "--..", "0": "-----", "1":".----", "2": "..----", "3": "...--",
    "4": "....-", "5":".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
}

reverse_symbols = {}
for letter in symbols:
    reverse_symbols[symbols[letter]] = letter

def encrypt(text):
    result = ""
    for ch in text.lower():
        if ch in symbols:
            result += symbols[ch] + " "
        else:
            return f"Error: Unknown character: {ch}"
    return result

def decrypt(morse):
    result = ""
    temp = ""
    for ch in morse:
        temp += ch
        if temp in reverse_symbols:
            result += reverse_symbols[temp]
            temp = ""
    if temp != "":
        return f"Error: Unknown Morse sequence: {temp}"
    return result

mode = input("Choose to Encrypt(e) or Decrypt(d): ")

if mode.lower() == "e":
    text = input("Enter the text: ")
    print("Encrypted: \n",encrypt(text))
elif mode.lower() == "d":
    morse = input("Enter the text: ")
    print("Decrypted: \n",decrypt(morse))
else:
    print("Invalid Input")
