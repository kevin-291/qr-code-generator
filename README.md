# QR Code Generator

This repository contains two Python scripts for generating QR codes. One script generates a basic QR code from a given URL, while the other generates a branded QR code with a custom logo in the center.

## Features

- Generate basic QR codes from URLs
- Generate branded QR codes with a custom logo
- Customize the color of the branded QR code
- Save the generated QR codes as PNG images

## Prerequisites

Before you can run these scripts, you need to have the following dependencies installed:

- Python 3.x
- Streamlit (for `app.py`)
- pyqrcode (for `app.py`)
- Pillow (for both scripts)
- qrcode (for `branded-qr-code.py`)

You can install the required packages using pip:

```bash
pip install streamlit pyqrcode Pillow qrcode
```

## Usage

### Basic QR Code Generator (`app.py`)

1. Run the `app.py` script with Streamlit:

```bash
streamlit run app.py
```

2. A web interface will open in your default browser.
3. Enter the URL you want to generate a QR code for.
4. The QR code will be generated and displayed on the web page.

### Branded QR Code Generator (`branded-qr-code.py`)

1. Make sure you have a logo image file (e.g., `input-logo.jpg`) in the same directory as the script.
2. Run the `branded-qr-code.py` script:

```bash
python branded-qr-code.py
```

3. The script will generate a branded QR code with the specified URL and logo, and save it as `logo.png` in the same directory.

## Customization

You can customize the branded QR code generator script by modifying the following variables:

- `Logo_link`: The file path of the logo image you want to use.
- `basewidth`: The base width of the logo image in pixels.
- `url`: The URL or text you want to encode in the QR code.
- `QRcolor`: The color of the QR code modules (e.g., 'Blue', 'Red', 'Green').

## Contributing

If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).