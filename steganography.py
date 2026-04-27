

from PIL import Image
import os

DELIMITER = '1111111111111110'  


def text_to_binary(text):
    """Convert a string to its binary representation."""
    return ''.join(format(ord(c), '08b') for c in text)


def embed_message(image_path, secret_text, output_path):
    """Hide secret_text inside an image using LSB steganography."""
    img = Image.open(image_path).convert('RGB')
    pixels = list(img.getflattened_data()) if hasattr(img, 'getflattened_data') else list(img.getdata()) # List of (R, G, B) tuples
    binary_message = text_to_binary(secret_text) + DELIMITER
    max_capacity = len(pixels) * 3  # 3 bits per pixel (R, G, B)

    if len(binary_message) > max_capacity:
        raise ValueError('Message too large for this image!')

    bit_index = 0
    new_pixels = []

    for pixel in pixels:
        r, g, b = pixel
        channels = [r, g, b]
        new_channels = []
        for ch in channels:
            if bit_index < len(binary_message):
                # Clear LSB and set to message bit
                ch = (ch & ~1) | int(binary_message[bit_index])
                bit_index += 1
            new_channels.append(ch)
        new_pixels.append(tuple(new_channels))

    stego_img = Image.new('RGB', img.size)
    stego_img.putdata(new_pixels)
    stego_img.save(output_path, 'PNG')
    print(f'[+] Message embedded. Stego image saved as: {output_path}')
    print(f'    Bits used: {bit_index} / {max_capacity}')


def extract_message(stego_path):
    """Extract hidden message from a stego image."""
    img = Image.open(stego_path).convert('RGB')
    pixels = list(img.getdata())
    binary_data = ''

    for pixel in pixels:
        for ch in pixel:
            binary_data += str(ch & 1)  

    message = ''
    for i in range(0, len(binary_data) - 16, 8):
        byte = binary_data[i:i+8]
        if binary_data[i:i+16] == DELIMITER:
            break  # End of message reached
        message += chr(int(byte, 2))

    return message


def show_image_info(image_path):
    """Display basic info about an image."""
    img = Image.open(image_path).convert('RGB')
    w, h = img.size
    capacity_chars = (w * h * 3) // 8
    print(f'    Image size   : {w} x {h} pixels')
    print(f'    Max capacity : ~{capacity_chars} characters')


if __name__ == '__main__':
    print('=' * 50)
    print('  Steganography Tool – LSB Image Encoding')
    print('  LA2 | Cryptography & Network Security')
    print('=' * 50)
    print()
    print('  1. Embed a secret message into an image')
    print('  2. Extract a hidden message from an image')
    print()
    choice = input('Choose option (1 or 2): ').strip()

    if choice == '1':
        img_path = input('Enter cover image path (PNG): ').strip()
        if not os.path.exists(img_path):
            print('[!] Image file not found.')
        else:
            show_image_info(img_path)
            message  = input('Enter secret message: ').strip()
            out_path = input('Output stego image name (e.g. stego.png): ').strip()
            try:
                embed_message(img_path, message, out_path)
            except ValueError as e:
                print(f'[!] Error: {e}')

    elif choice == '2':
        stego_path = input('Enter stego image path (PNG): ').strip()
        if not os.path.exists(stego_path):
            print('[!] Stego image file not found.')
        else:
            result = extract_message(stego_path)
            print(f'\n[+] Hidden message recovered:')
            print(f'    {result}')

    else:
        print('[!] Invalid choice. Please enter 1 or 2.')
