#-----------------------------------------------------------------
#                    CRYPTOGRAPHY MODULE
#                  -----------------------
# This program is used to perform the cryptographic operations like hashing, RSA Digital Signature,
#  RSA Encryption and RSA Decryption.
# The sender will perform the hashing, RSA Digital Signature , RSA Encryption ,
#  send the cipher text to the receiver.
#  The receiver will perform the RSA Decryption and RSA Digital Signature Decryption to verify 
# the authenticity of the sender and then decrypt the secret message.
# The sender and receiver will communicate through a socket connection.
# After the authentication is done , the sender will send the secret message to the receiver in a confidential way.
# The receiver will verify the authenticity of the sender and then decrypt the secret message to make sure that
# the message is coming from the sender and not from an intruder.
# The program is divided into two parts :
# 1. The sender set-up
# 2. The receiver set-up

# Author Details :- 
# Name = Hemanth Gowda A
# gmail = hemanth18gowda01@gmail.com
# Linkedin URL = https://www.linkedin.com/in/hemanth-gowda-a-a7146a372?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app
#--------------------------------------------------------------------

import hashlib as hs 

#-----------------------------------------------------------------
#                    THE SENDER SET-UP
#-----------------------------------------------------------------

def hashing_file(file_name):
    f = open(file_name,'r')
    data = f.read()
    f.close()
    hash_input = data.encode('utf-8')
    hash_code = hs.sha256(hash_input).hexdigest()
    return hash_code

#----------------------------------------------------
# In RSA Digital Signature , i will take things like :
# Sender's Detail
#----------------------------------------------------

def RSA_digital_signature(hash_code):
    n1 = 11462790376655076215907553793975759885815845366422742587488335774628555337721800284303112611806159602879170563236141391142955213929126572817018729220905657798423847938467116905337501
    d1 = 104943378946137994255833075612027647458527354316701184864931282554543741743337048851516968475980806450449153065730898809093530930884218019981309857486092816070208118936584781731073
    hash_code_int = int(hash_code,16)
    Intermediate_Cipher_text = pow(hash_code_int,d1,n1)
    return Intermediate_Cipher_text


#-----------------------------------------------------
# In RSA Encryption , i will take things like :
# Receiver's Detail
#-----------------------------------------------------

def RSA_encryption(encrypted_code_int):
    n2 = 92398692951600629630504081614781327139784109293869112997009867829105221031347730539873606195690008475237182773406498185659171760062088717874523724718184071350018986539855034915311606038550958987526667287287277079496626397937033784744807308614850832639207144730536428947738216932826618496931256356606952609816400686594938629885374144381530216950058714264554308292473970160931252164803647137156759852418657150430746251729721
    e2 = 65537
    Cipher_text = pow(encrypted_code_int,e2,n2)
    return Cipher_text


#-------------------------------------------------------------------
#                              END
#------------------------------------------------------------------- 


#-------------------------------------------------------------------
#                       THE RECEIVER SET-UP
#-------------------------------------------------------------------

def RSA_decryption(Sender_Cipher_text):
    n2 = 92398692951600629630504081614781327139784109293869112997009867829105221031347730539873606195690008475237182773406498185659171760062088717874523724718184071350018986539855034915311606038550958987526667287287277079496626397937033784744807308614850832639207144730536428947738216932826618496931256356606952609816400686594938629885374144381530216950058714264554308292473970160931252164803647137156759852418657150430746251729721
    d2 = 52158164788508251723156362044933933465619621333394690561429117297675323131280182054757222045707796565930689178665080799830035846369180342673116029051516238454521146940536445316263375885319632081778980671882948789893581398986733096555386428104896993313890915958512893971676089743461436421296029338427944531735158378872175041160801742732088637530879320041527125737658117266650443346931836405310299695690648331898708344169693
    decrypted_code = pow(Sender_Cipher_text,d2,n2)
    return decrypted_code


def RSA_Decrypted_DS(decrypted_code):
    n1 = 11462790376655076215907553793975759885815845366422742587488335774628555337721800284303112611806159602879170563236141391142955213929126572817018729220905657798423847938467116905337501
    e1 = 65537
    decrypted_hash_code = pow(decrypted_code,e1,n1)
    hash_code = format(decrypted_hash_code, '064x')
    return hash_code


#----------------------------------------------------------------------
#                             END 
#----------------------------------------------------------------------

#----------------------------------------------------------------------
#    CONFIDENTIAL COMMUNICATION AFTER CONFIDENTIAL AUTHENTICATION
#----------------------------------------------------------------------


def sender():
    message = input("Enter the message : ")
    f = open(message,'r')
    data = f.read()
    f.close()
    n2 = 92398692951600629630504081614781327139784109293869112997009867829105221031347730539873606195690008475237182773406498185659171760062088717874523724718184071350018986539855034915311606038550958987526667287287277079496626397937033784744807308614850832639207144730536428947738216932826618496931256356606952609816400686594938629885374144381530216950058714264554308292473970160931252164803647137156759852418657150430746251729721
    e2 = 65537
    plain_text = data.encode('utf-8')
    plain_text_int = int.from_bytes(plain_text, byteorder='big')
    Cipher_text = pow(plain_text_int,e2,n2)
    return Cipher_text

def receiver(verification_hash_code, decrypted_hash_code, secret_message):
    n2 = 92398692951600629630504081614781327139784109293869112997009867829105221031347730539873606195690008475237182773406498185659171760062088717874523724718184071350018986539855034915311606038550958987526667287287277079496626397937033784744807308614850832639207144730536428947738216932826618496931256356606952609816400686594938629885374144381530216950058714264554308292473970160931252164803647137156759852418657150430746251729721
    d2 = 52158164788508251723156362044933933465619621333394690561429117297675323131280182054757222045707796565930689178665080799830035846369180342673116029051516238454521146940536445316263375885319632081778980671882948789893581398986733096555386428104896993313890915958512893971676089743461436421296029338427944531735158378872175041160801742732088637530879320041527125737658117266650443346931836405310299695690648331898708344169693
    
    if verification_hash_code == decrypted_hash_code:
        decrypted_int = pow(secret_message ,d2,n2)
        decrypted_bytes = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, byteorder='big')
        decrypted_message = decrypted_bytes.decode('utf-8')
        result = print("Verification is done \nThe message is coming from sender.....\nThe secret message is : \n{}".format(decrypted_message))
                
    else:
        result = print("Verification Failed\nThe message is not coming from sender\n Might be coming from an intruder.....")
    return result

#-------------------------------------------------------------------------
#                        END OF THE PROGRAM
#-------------------------------------------------------------------------












