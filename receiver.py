import socket
import tqdm
from Crypto.Cipher import AES   
import hashlib


nonce = b"networking123456"
key = b"network123456789"

# ciphers and hashes for confidentiality and integrity
cipher = AES.new(key, AES.MODE_EAX, nonce)
#cipher.update()
hash = hashlib.md5()

# Creating a socket instance
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 4000

# Establishing TCP connection to transfer files
server.bind(('0.0.0.0', port))    
server.listen()

client, addr = server.accept()

# Receive the file name
file_name = client.recv(1024).decode(encoding="utf-8", errors="ignore")

# Receive the file size as a byte string
file_size_bytes = client.recv(8)

# Convert the file size byte string to an integer
file_size = int.from_bytes(file_size_bytes, byteorder="big")

print("Receiving " + str(file_name) + " of size " + str(file_size))

recv_file_name = "recv_" + str(file_name)
recv_file = open(recv_file_name, "wb")
finished = False
recv_file_bytes = b""

while not finished:
    data = client.recv(1024)
    if recv_file_bytes[-7:] == b"(DONE:)":
        finished = True
    else:
        recv_file_bytes += data

decrypt_data = cipher.decrypt(recv_file_bytes[:-7])
hash.update(decrypt_data)

received_hash = client.recv(16)
'''
if hash.digest() == received_hash:
    print("File integrity check succeeded.")
    
else:
    print("File integrity check failed.")
'''

recv_file.write(decrypt_data)

recv_file.close()
client.close()
server.close()
