import os
import requests

# Set your DeepL API key
DEEPL_API_KEY = "c225788c-340d-468e-9ecb-9a3eaa9512d8:fx"
DEEPL_URL = "https://api-free.deepl.com/v2/document"

# Function to upload a PDF file to DeepL for translation
def upload_pdf(file_path, target_language):
    with open(file_path, 'rb') as file:
        response = requests.post(
            DEEPL_URL,
            headers={
                "Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}"
            },
            data={
                "file": file,
                "target_lang": target_language
            }
        )
        
    if response.status_code == 200:
        print(f"Successfully uploaded: {file_path}")
        return response.json()
    else:
        print(f"Failed to upload {file_path}: {response.status_code} - {response.text}")
        return None

# Main function to upload all PDFs in a specified directory
def upload_all_pdfs(directory, target_language="ZH"):
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            file_path = os.path.join(directory, filename)
            upload_pdf(file_path, target_language)

# Specify the directory containing PDF files and the target language code
pdf_directory = "C:/Users/cbes1/Desktop/Python"  # Change this to your directory path
upload_all_pdfs(pdf_directory)