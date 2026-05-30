import socket
import crypto
from crypto import hashing_file, RSA_digital_signature, RSA_encryption

#----------------------------------------------------------------
#                THE SENDER SETTING UP SERVER
#----------------------------------------------------------------
c = socket.socket()
c.connect(("localhost",8000))

name = input("Enter your name : ")
file_name = input("Enter the hash key : ")

#---------------------------------------------------------------------------------------
# SECURE HASHING OF THE FILE AND ENCRYPTION OF THE HASH CODE USING RSA DIGITAL SIGNATURE
#---------------------------------------------------------------------------------------

hash_code = hashing_file(file_name)
print("The hash code is :", hash_code)

encrypted_hash = RSA_digital_signature(hash_code)
print("Encrypted Authenticity hash code is :", encrypted_hash)

Cipher_text = RSA_encryption(encrypted_hash)
print("Cipher text is :", Cipher_text)

c.send(bytes(name,'utf-8'))
c.send(bytes(str(Cipher_text),'utf-8'))

#-------------------------------------------------------------------------
#    REPEATED CONFIDENTIAL COMMUNICATION AFTER CONFIDENTIAL AUTHENTICATION
#-------------------------------------------------------------------------

while True :
    
    confidential_message = crypto.sender()
    print("The message sent by you is : ",confidential_message)

    c.send(bytes(str(hash_code) + str(confidential_message),'utf-8'))
    response = c.recv(1024).decode()

    print("Receiver says: ", response)

#-------------------------------------------------------------------
#                  END OF THE COMMUNICATION
#-------------------------------------------------------------------
    

