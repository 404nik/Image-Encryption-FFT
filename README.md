# Image Encryption and Decryption using Fourier Transform

This project provides a Python implementation for encrypting and decrypting images using Fourier Transform techniques. The encryption process involves transforming the image into the frequency domain, mutating the frequency components, and then transforming it back into the spatial domain. Decryption reverses this process to recover the original image.

## Features

- Encryption and decryption of grayscale as well as RGB images.
- Customizable encryption keys to enhance security.
- Supports both single-channel (grayscale) and three-channel (RGB) images.

## Requirements

- Python 3.x
- NumPy
- Pillow (PIL)

## Installation

1. Clone this repository:

    ```
    git clone https://github.com/your-username/image-encryption.git
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Import the necessary modules:

    ```python
    import numpy as np
    from PIL import Image
    ```

2. Use the provided functions to encrypt and decrypt images:

    ```python
    # Encrypt an image
    mainencrypt("input_image.jpg", key)

    # Decrypt an image
    maindecrypt("encrypted_image.jpg", key)
    ```

    Replace `"input_image.jpg"` and `"encrypted_image.jpg"` with the paths to your input image and encrypted image, respectively. Replace `key` with your chosen encryption key.
