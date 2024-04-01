import cv2
import numpy as np

def message2binary(message):
    binary_data = ''.join(format(ord(char), '08b') for char in message)
    return binary_data

def encode_data(img):
    # Read text data from a file
    filename = input("Enter the name of the file containing text data:")
    with open(filename, 'r') as file:
        data = file.read()

    if len(data) == 0:
        raise ValueError('Data is empty')

    new_filename = input("Enter the name of the New Image after Encoding (with extension):")

    no_bytes = (img.shape[0] * img.shape[1] * 3) // 8

    print("Maximum bytes to encode:", no_bytes)

    if len(data) > no_bytes:
        raise ValueError("Error encountered: Insufficient bytes. Need a bigger image or less data!")

    # Using the below as delimiter
    data += '*****'

    data_binary = message2binary(data)
    data_len = len(data_binary)

    print("The Length of Binary data:", data_len)

    data_index = 0

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):
                if data_index < data_len:
                    pixel = img[i, j, k]
                    binary_pixel = format(pixel, '08b')[:-1] + data_binary[data_index]
                    img[i, j, k] = int(binary_pixel, 2)
                    data_index += 1

                if data_index >= data_len:
                    break
            if data_index >= data_len:
                break

        if data_index >= data_len:
            break

    cv2.imwrite(new_filename, img)

    print("Encoded the data successfully and the image is successfully saved as:", new_filename)

# Example usage:
# Load an image
img = cv2.imread("input_image.png")
# Encode data into the image
encode_data(img)
