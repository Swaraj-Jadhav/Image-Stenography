# Image Stenography
## Overview
This project demonstrates image steganography, a technique for hiding secret messages inside images by modifying pixel values. The message is encoded into the least significant bits (LSBs) of image pixels, allowing for secure data concealment.

## Features
- Hide a secret message inside an image.
- Retrieve the hidden message with a passcode.
- Uses a termination character (`~`) to mark the end of the message.
- Ensures message does not exceed image capacity.

## Technologies Used
- Python
- OpenCV (cv2) for image processing
