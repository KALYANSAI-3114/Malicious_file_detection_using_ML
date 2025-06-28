def extract_signature_bytes(file_path, max_len=256):
    with open(file_path, 'rb') as f:
        byte_data = f.read(max_len)
    byte_vector = [b for b in byte_data]
    byte_vector += [0] * (max_len - len(byte_vector))
    return byte_vector[:max_len]
