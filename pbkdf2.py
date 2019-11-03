
from Crypto.Cipher import AES
import os
#import PBKDF2
import pbkdf2

#from pbkdf2 import pbkdf2
salt = os.urandom(8)    # 64-bit salt
key = pbkdf2("This passphrase is a secret.", salt).read(32) # 256-bit key
iv = os.urandom(16)     # 128-bit IV
cipher = AES.new(key, AES.MODE_CBC, iv)

