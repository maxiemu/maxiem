
msg = input("Enter a message to encrypt: ")
encmsg = ""
for ch in msg:
    asc = ord(ch) + 3
    ench = chr(asc)
    encmsg += ench
print("Encrypted message:",encmsg)