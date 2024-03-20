import streamlit as st
import pyqrcode
from PIL import Image

st.title("QR Code Generator")

# Function to generate QR code
def generate_qr_code(website_url):
    qr = pyqrcode.create(website_url)
    qr_image = qr.png('qr_code.png', scale=6)
    return qr_image

# Main function
def main():
    # Input box for website URL
    website_url = st.text_input("Enter the website URL:")
    
    # Check if the URL is provided
    if website_url:
        # Generate QR code
        qr_image = generate_qr_code(website_url)
        
        # Display QR code
        st.image('qr_code.png', caption='Generated QR Code', use_column_width=True)
    else:
        st.info("Please enter a website URL.")

if __name__ == "__main__":
    main()
