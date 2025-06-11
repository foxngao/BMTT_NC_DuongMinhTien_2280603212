import hashlib

def blank_hash(message):
    blank_hash = hashlib.blake2b(digest_size=64)
    blank_hash.update(message)
    return blank_hash.digest()

def main():
    text = input("Enter message to hash: ").encode('utf-8')
    hashed_text = blank_hash(text)
    
    print("Original message:", text.decode('utf-8'))
    print("BLAKE2b Hash:", hashed_text.hex())

if __name__ == "__main__":
    main()
