# Secure-FIle-Transfer
This repository contains the code for secure file transfer between sender and receiver present in the same network.
Change the ip address in the sender code and the code should work just fine. I have ignored the secure key exchange between sender and receiver. For more information on 
secure key exchange, check out Diffie Helmann Key Exchange protocol.This project has been implemented using sockets module in python in additon to 'pycryptodomex' for encryption. 

Any file format can be transferred using this code as the contents of the file are read as bytes and then encrypted using a 16 bit AES key.

