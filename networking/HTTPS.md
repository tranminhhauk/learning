# 1.What is HTTPS ?
- HTTPS is the secure version of HTTP, this protocol used to send data between web browser and web server
- HTTPS is particularly important when users transmit sensitive data, such a logging into bank account, email service
- websites do not use HTTPS are marked differently than those that are (padlock in URL)
# 2. How does HTTPS work ?
- HTTPS uses an encryption protocol to encrypt communications called TLS
- It includes two processes:
    - process HandShake/ authentication
    -> used Asymmetric encryption
    - process data transmission
    -> used Symetric encryption

a) Asymmetric Encryption

    -Uses a key pair: Public Key and Private Key.
    
    -Private Key: This key lives on a web server and is used to decrypt information encrypted by the public key.

    -Public Key: this key is available to anyone who wants to interact with the server securely. Information encrypted with the public key can only be decrypted using the private key.

b) Symmetric Encryption

    -Uses a single shared key: Session Key.

    - Session Key: This key is temporary and is independently calculated by both the client and the server during the handshake.

    - Purpose: This same key is used by both sides to quickly encrypt and decrypt the actual data transmission

NOTE: 
- Session key will be initiated on both the client and server during the handshake process
- But in asymmetric, public key and private key managed by server and public keys are only transmitted client by the server

# 3. Why is HTTPS important?

HTTPS prevents third parties from detecting the data transmission process between the client and the server because even if they did detect it, without the decryption key, they would only receive a meaningless string of characters.

- Exmple: 
- Before encryption
    - This is a string of text 

- After encryption:
    - ITM0IRyiEhVpa6VnKyExMiEgNveroyWBPlgGyfkflYjDaaFf/Kn3bo3OfghBPDWo6AfSHl