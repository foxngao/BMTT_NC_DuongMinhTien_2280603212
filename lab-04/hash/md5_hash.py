def left_rotate(value, shift, bits=32):
    return ((value << shift) | (value >> (bits - shift))) & 0xFFFFFFFF

def custom_md5(message):
    # Khởi tạo giá trị ban đầu (giống MD5 thật)
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    # Chuẩn bị thông điệp
    original_length = len(message)
    message = bytearray(message)
    
    # Thêm padding
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0x00)
    
    # Thêm độ dài ban đầu (little-endian)
    message += original_length.to_bytes(8, 'little')

    # Xử lý từng khối 512-bit (64-byte)
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]

        aa, bb, cc, dd = a, b, c, d

        # Vòng lặp chính
        for j in range(64):
            if j < 16:
                f = (bb & cc) | ((~bb) & dd)
                g = j
            elif j < 32:
                f = (dd & bb) | ((~dd) & cc)
                g = (5*j + 1) % 16
            elif j < 48:
                f = bb ^ cc ^ dd
                g = (3*j + 5) % 16
            else:
                f = cc ^ (bb | (~dd))
                g = (7*j) % 16

            temp = dd
            dd = cc
            cc = bb
            bb = (bb + left_rotate((aa + f + 0x100000000 + words[g]) & 0xFFFFFFFF, [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
                    5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
                    4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
                    6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21][j])) & 0xFFFFFFFF
            aa = temp

        a = (a + aa) & 0xFFFFFFFF
        b = (b + bb) & 0xFFFFFFFF
        c = (c + cc) & 0xFFFFFFFF
        d = (d + dd) & 0xFFFFFFFF

    # Kết hợp kết quả và trả về
    return (a.to_bytes(4, 'little') + b.to_bytes(4, 'little') + 
            c.to_bytes(4, 'little') + d.to_bytes(4, 'little')).hex()

input_str = input("Nhập chuỗi: ")
hash_result = custom_md5(input_str.encode())
print(f"MD5 của '{input_str}' là: {hash_result}")
