from PyPDF2 import PdfReader, PdfWriter

def encrypt_pdf(input_path, output_path, password):
    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(password)

        with open(output_path, "wb") as f:
            writer.write(f)

        print(f"Encrypted PDF saved as '{output_path}'")

    except FileNotFoundError:
        print("Input PDF file not found.")
    except Exception as e:
        print(f"Error: {e}")

# Get inputs from user
input_file = input("Enter the path to the input PDF: ")
output_file = input("Enter the name of the output PDF: ")
password = input("Enter the password to protect the PDF: ")

encrypt_pdf(input_file, output_file, password)
