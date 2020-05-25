from random import randint
from re import findall

cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
    print("Error: mode is not found")
    raise SystemExit
startMessage = input("Write the message: ")
def regular(text):
    return findall(r"[0-9]+", text)
def encryptDecrypt(mode, message, final = [], keys = []):
    if mode == 'E':
        for symbol in message:
            key = randint(0,25); keys.append(str(key))
            final.append(str(ord(symbol) ^ key))
        return '.'.join(final), '.'.join(keys)
    else:
        keys = input("Write the keys: ")
        for index, symbol in enumerate(regular(message)):
            final.append(chr(int(symbol) ^ int(regular(keys)[index])))
        return ''.join(final)

print("Final message:",encryptDecrypt(cryptMode, startMessage))


#1) Run the code
#2) To encode the selected text, type "E" in the console and insert the desired text
#3) To decode the desired text, type in the console "D", in the next field, insert the code and press Enter; in the next field, insert the decryption key and press Enter
#
#In order for the code to work, you need to download or have  downloaded a python!!!
#
#This code is a simple Encrypt | Decrypt code based on the XOR Wiegener cipher