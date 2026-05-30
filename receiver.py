import socket
import crypto 
#----------------------------------------------------------------
#                   THE RECEIVER SET-UP 
#----------------------------------------------------------------
s = socket.socket()
print("Socket created..")

#----------------------------------------------------------------
#                  SERVER SET-UP
#----------------------------------------------------------------
s.bind(('localhost',8000))
s.listen(5)

print("Waiting for connections..!!")

#----------------------------------------------------------------
#                   COMMUNICATION SET-UP
#----------------------------------------------------------------

while True :
    c,addr = s.accept()
    name = c.recv(1024).decode()
    Cipher_text = c.recv(1024).decode()

    c.send(bytes("Welcome to My Server",'utf-8'))
    print("Connected with ",addr , name)
    auth_result={}

    print("Cipher text received from sender is : ",Cipher_text)
    decrypted_code = crypto.RSA_decryption(int(Cipher_text))

    print("Decrypted Digital Signature code is : ",decrypted_code)
    decrypted_hash_code = crypto.RSA_Decrypted_DS(decrypted_code)

    print("Decrypted Authenticity hash code is : ",decrypted_hash_code)

    #-------------------------------------------------------------------
    #    REPEATED CONFIDENTIAL COMMUNICATION AFTER CONFIDENTIAL AUTHENTICATION
    #-------------------------------------------------------------------
    while True:
        auth_confidential_message = c.recv(1024).decode()
        if not auth_confidential_message:
            break

        verification_code = str(auth_confidential_message)
        verification_hash_code = verification_code[:64]
        secret_message = int(verification_code[64:])
        auth_result[verification_hash_code] = secret_message
        print(verification_hash_code)

        original_message = crypto.receiver(verification_hash_code, decrypted_hash_code, secret_message)
        print(original_message)

        c.send(bytes("Message received and verified","utf-8"))
    
    c.close()

#-------------------------------------------------------------------
#                  END OF THE COMMUNICATION
#-------------------------------------------------------------------
        
        
    
    


    