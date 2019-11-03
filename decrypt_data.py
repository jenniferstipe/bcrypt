
#example from https://www.pycryptodome.org/en/latest/src/examples.html#encrypt-data-with-aes

from Crypto.Cipher import AES

file_in = open("encrypted.bin", "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

key=b'Z\xe63Q\xb4spt\xef\xe6\xc7\xda\xf0\xf5]\xd4'
# let's assume that the key is somehow available again
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print(data)