def decrypt(cipher,s):
    result = ""
 
    for i in range(len(cipher)):
        char = cipher[i]
 
        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)
 
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
 
    return result
 
cipher = " RIXVErEKKEVAEP "
s = 4
print ("cipher  : " + cipher)
print ("Shift : " + str(s))
print ("text: " + decrypt(cipher,s))
