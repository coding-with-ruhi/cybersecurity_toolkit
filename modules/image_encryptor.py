# Image Encryption and Decryption Tool
# Cybersecurity Internship - Task 2

from PIL import Image

def encrypt_decrypt_image(input_path, output_path, key):
    
    # Open image and convert to RGB (removes alpha channel issues)
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()

    width, height = img.size

    # Loop through every pixel
    for x in range(width):
        for y in range(height):

            r, g, b = pixels[x, y]

            # XOR encryption
            r = r ^ key
            g = g ^ key
            b = b ^ key

            pixels[x, y] = (r, g, b)

    img.save(output_path)
    print("\nProcess completed successfully!")
    print("Output image saved as:", output_path)


print("====== Image Encryption Tool ======")

input_image = input("Enter input image path: ")
output_image = input("Enter output image path: ")
key = int(input("Enter encryption key (0-255): "))

encrypt_decrypt_image(input_image, output_image, key)