import pdfkit
import os

# Define the directory containing the HTML files
html_directory = 'novel_pages'
# Define the output directory for PDFs
pdf_directory = 'novel_pdfs'
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Adjust this path as needed

# Create the output directory if it doesn't exist
os.makedirs(pdf_directory, exist_ok=True)

# Loop through pages 1 to 100
for page_number in range(1, 101):
    # Construct the file names
    html_file = os.path.join(html_directory, f'page_{page_number}.html')
    pdf_file = os.path.join(pdf_directory, f'page_{page_number}.pdf')
    
    # Check if the HTML file exists
    if os.path.exists(html_file):
        try:
            # Convert HTML to PDF with options
            pdfkit.from_file(html_file, pdf_file, options={'no-stop-slow-scripts': ''})
            print(f"Converted: {html_file} to {pdf_file}")
        except Exception as e:
            print(f"Error converting {html_file}: {e}")
    else:
        print(f"HTML file not found: {html_file}")