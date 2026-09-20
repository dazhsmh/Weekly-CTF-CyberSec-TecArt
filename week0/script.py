from Crypto . Cipher import AES
from Crypto . Random import get_random_bytes
key = get_random_bytes (16)
data = b" Hello PyCryptodome !"
cipher = AES . new ( key , AES . MODE_EAX )
ciphertext , tag = cipher . encrypt_and_digest ( data )
print (" Ciphertext :", ciphertext .hex () )
cipher = AES . new ( key , AES . MODE_EAX , nonce = cipher . nonce )
plaintext = cipher . decrypt ( ciphertext )
print (" Plaintext :", plaintext . decode () )
