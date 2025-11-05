from PIL import Image

def encode(image_path, text, output_path):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    text_length = len(text)
    if text_length > width * height - 1:
        print("your text is so higher, lower your text or increase your image size!")
        return

    pixels[0, 0] = (text_length, 0, 0)

    idx = 0
    for y in range(height):
        for x in range(width):
            if x == 0 and y == 0:
                continue
            if idx < text_length:
                char_code = ord(text[idx])
                r, g, b = pixels[x, y]
                pixels[x, y] = (char_code, g, b)
                idx += 1
            else:
                break
        if idx >= text_length:
            break

    img.save(output_path)
    print("encoding success!! save to:", output_path)

def decode(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    text_length = pixels[0, 0][0]

    text = ""
    idx = 0
    for y in range(height):
        for x in range(width):
            if x == 0 and y == 0:
                continue
            if idx < text_length:
                r, g, b = pixels[x, y]
                text += chr(r)
                idx += 1
            else:
                break
        if idx >= text_length:
            break

    img.close()
    print("coded text:\n", text)

encode('images.bmp', 'hellow im hossein', 'coded.bmp')

decode('coded.bmp')
