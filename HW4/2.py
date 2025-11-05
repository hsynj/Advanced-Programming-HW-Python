from PIL import Image
import random

file = open('3.txt', 'w')
file2 = open('3.txt', 'r')

img = Image.open('images.bmp')
pixels = img.load()
width, height = img.size
rand_num1 = random.randint(0, width)
rand_num2= random.randint(0, height)
def encode():
    final_msg = ''
    
    r, g, b = pixels[rand_num1, rand_num2]
    r_bin = bin(r)[2:]
    g_bin = bin(g)[2:]
    b_bin = bin(b)[2:]

    combine_bits = r_bin + g_bin + b_bin + '1'

    five_fives = [combine_bits[i:i+5] for i in range(0, 25, 5)]
    final = ['010' + five for five in five_fives]
    decoded = [chr(int(byte, 2)) for byte in final]

    final_msg = final_msg.join(decoded)
    file.write(final_msg)
    file.close()


def decode(message):
    binary_chunks = [format(ord(char), '08b') for char in message]
    five_bit_chunks = [chunk[3:] for chunk in binary_chunks]
    combined_25_bits = ''.join(five_bit_chunks)
    combined_24_bits = combined_25_bits[:-1]

    r_bin = combined_24_bits[0:8]
    g_bin = combined_24_bits[8:16]
    b_bin = combined_24_bits[16:24]
    r = int(r_bin, 2)
    g = int(g_bin, 2)
    b = int(b_bin, 2)

    return (r, g, b)


encode()

message = file2.read()
rgb = decode(message)

print("RGB Code: ")
print(rgb)

