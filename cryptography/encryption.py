# encryption using symmetric way
def encrypt(str , key=2):
    return ''.join(chr(ord(c)+2) for c in str)
print("encrypted text : " ,encrypt("ABC"))

def decrypt(str,key=2):
    return ''.join(chr(ord(c)-2) for c in str)

print("decrypted text : ", decrypt("CDE"))