import os
from cryptography.fernet import Fernet

def decrypt(key, output_path, files):
    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
        decrypted_data = Fernet(key).decrypt(file_data)
        filename = os.path.basename(file)
        decrypted_filename = filename.rsplit('.enc', 1)[0]
        output_file = os.path.join(output_path, decrypted_file)
        with open(output_file, 'wb') as f:
            f.write(decrypted_data)

    return True
