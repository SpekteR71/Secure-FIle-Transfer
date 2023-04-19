import socket
import tqdm
from Cryptodome.Cipher import AES
import hashlib
import os

nonce = b"networking123456"
key = b"network123456789"

# ciphers and hashes for confidentiality and integrity
cipher = AES.new(key, AES.MODE_EAX, nonce)
hash = hashlib.md5()

# Creating a socket instance
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Setting the IP address and port number 
server_ip = "192.168.43.154"
server_port = 4000

# Establishing TCP connection to transfer files
client.connect((server_ip, server_port))

# Sending the file name 
file_name = "wp1809881-suicide-squad-wallpapers.jpg"
client.send(file_name.encode(encoding="utf-8", errors="ignore"))

# Sending the file size as a byte string
file_size = os.path.getsize(file_name)
client.send(file_size.to_bytes(8, byteorder="big"))

print("Sending " + str(file_name) + " of size " + str(file_size))

progress_bar = tqdm.tqdm(unit = "B", unit_scale = True, unit_divisor = 1024, total = file_size)

with open(file_name, "rb") as f:
    while True:
        # Reading and encrypting the file data
        data = f.read(1024)
        if not data:
            break
        encrypt_data = cipher.encrypt(data)
        hash_value = hash.update(encrypt_data)
        
        # Sending the encrypted file data 
        client.sendall(encrypt_data)
        progress_bar.update(len(data))  

    #client.send(hash.digest())    

# Sending the "done" message 
done_message = "DONE:)"
client.sendall(done_message.encode())

client.close()