#pip install pytesseract pdf2image Pillow
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# If you're using Windows, provide the path to the tesseract executable.
# Uncomment the following line if needed.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# ... existing code ...

import os

def pdf_to_text(pdf_path):
    # Path to the Poppler bin folder
    poppler_path = r'C:\poppler\Library\bin'  # Update this with the correct path where you extracted Poppler

    # Convert PDF pages to images
    images = convert_from_path(pdf_path, poppler_path=poppler_path)

    # Initialize an empty string to hold the text
    extracted_text = ""

    # Iterate over the images (one image per page)
    for i, image in enumerate(images):
        # Convert the image to text using pytesseract
        page_text = pytesseract.image_to_string(image)
        extracted_text += f"Page {i + 1}:\n{page_text}\n\n"

    return extracted_text

# Example usage
pdf_path = r"C:\py\gedni.pdf"  # Replace with the path to your PDF file
text = pdf_to_text(pdf_path)

# Generate the output text file path
output_path = os.path.splitext(pdf_path)[0] + ".txt"

# Output the extracted text to a text file
with open(output_path, "w", encoding="utf-8") as text_file:
    text_file.write(text)

print(f"Extracted text has been saved to {output_path}")