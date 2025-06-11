import hashlib

def calculate_sha3_hash(data):
    sha3_hash = hashlib.sha256()
    sha3_hash.update(data.encode("utf-8"))
    return sha3_hash.hexdigest()

data_to_hash = input("Nhập dữ liệu cần hash: ")
hash_value = calculate_sha3_hash(data_to_hash)
print("Giá trị hash SHA-256:", hash_value)
