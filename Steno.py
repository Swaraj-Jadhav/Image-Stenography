import cv2 
import os

def encode_message(image_path, output_path, message, password):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return

    rows, cols, channels = img.shape
    max_length = rows * cols * 3  
    
    if len(message) + 1 > max_length:  
        print("Error: Message too long for the image size.")
        return

    # Append a termination character (e.g., '~') to mark the end
    message += "~"

    index = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(3):  # Iterate over R, G, B
                if index < len(message):
                    img[i, j, k] = ord(message[index])  # Store ASCII value
                    index += 1
                else:
                    break  # Stop if message encoding is done

    cv2.imwrite(output_path, img)
    print("Message encoded successfully in", output_path)

def decode_message(image_path, password):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return
    
    rows, cols, channels = img.shape
    message = ""

    for i in range(rows):
        for j in range(cols):
            for k in range(3):
                char = chr(img[i, j, k])  # Retrieve ASCII character
                if char == "~": 
                    print("Decrypted message:", message)
                    return
                message += char

    print("Decrypted message:", message)

# Usage
image_path = "D:\Cybersecurity\Input_Img.jpg"
output_path = "D:\Cybersecurity\Encrypted_Img.jpg"

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

encode_message(image_path, output_path, msg, password)

# Decryption
pas = input("Enter passcode for Decryption: ")
if pas == password:
    decode_message(output_path, pas)
else:
    print("YOU ARE NOT AUTHORIZED")
