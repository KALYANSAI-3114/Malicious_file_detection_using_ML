import os

os.makedirs("data/benign_samples", exist_ok=True)
os.makedirs("data/malicious_samples", exist_ok=True)

# Benign: repeated low-entropy content
for i in range(5):
    with open(f"data/benign_samples/benign_{i}.bin", "wb") as f:
        f.write(b"\x10\x20\x30\x40\x50" * 50)  # 250 bytes

# Malicious: random high-entropy content
for i in range(5):
    with open(f"data/malicious_samples/malicious_{i}.bin", "wb") as f:
        f.write(os.urandom(256))
