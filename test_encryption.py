from PyPDF2 import PdfReader

def is_encrypted(file_path):
    try:
        reader = PdfReader(file_path)
        return reader.is_encrypted
    except Exception as e:
        print(f"Error: {e}")
        return False

# Example
file = input("Enter file name to check: ")
print("Encrypted:", is_encrypted(file))
