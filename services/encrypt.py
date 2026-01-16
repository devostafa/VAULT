from cryptography.fernet import Fernet
import os

def encrypt(key, output_path, files):
    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
        encrypted_data = Fernet(key).encrypt(file_data)
        filename = os.path.basename(file)
        encrypted_file = f'{filename}.enc'
        output_file = os.path.join(output_path, encrypted_file)
        with open(output_file, 'wb') as f:
            f.write(encrypted_data)

    return True