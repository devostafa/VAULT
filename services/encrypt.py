import os
import base64
from cryptography.fernet import Fernet

def encrypt(key, output_path, files):
    crypt_key = base64.urlsafe_b64encode(key.zfill(32).encode()) # Weak way to pad key to 32 bytes
    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
        encrypted_data = Fernet(crypt_key).encrypt(file_data)
        filename = os.path.basename(file)
        encrypted_filename = f'{filename}.enc'
        output_file = os.path.join(output_path, encrypted_filename)
        with open(output_file, 'wb') as o:
            o.write(encrypted_data)

    return True