import os
import base64
from cryptography.fernet import Fernet

def decrypt(key, output_path, files):
    crypt_key = base64.urlsafe_b64encode(key.zfill(32).encode()) # Weak way to pad key to 32 bytes
    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
        decrypted_data = Fernet(crypt_key).decrypt(file_data)
        filename = os.path.basename(file)
        decrypted_filename = filename.rsplit('.enc', 1)[0]
        output_file = os.path.join(output_path, decrypted_filename)
        with open(output_file, 'wb') as o:
            o.write(decrypted_data)

    return True
