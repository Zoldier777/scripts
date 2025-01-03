import sys
from PyPDF2 import PdfReader, PdfWriter


def trim_pdf(input_file, num_pages):

    if not input_file.lower().endswith('.pdf'):
        print("Error: The input file must be a PDF (.pdf).")
        sys.exit(1)

    reader = PdfReader(input_file)
    writer = PdfWriter()

    num_pages = min(num_pages, len(reader.pages))

    for i in range(num_pages):
        writer.add_page(reader.pages[i])

    output_file = f"{input_file[:-4]}-{num_pages}-pages.pdf"  

    with open(output_file,"wb") as f:
        writer.write(f)
    print("Done")

def main():
    if len(sys.argv) < 3:
        print("Usage: python trim_pdf.py <input_file> <num_pages>")
        sys.exit(1)
    input_file = sys.argv[1]
    try:
        num_pages = int(sys.argv[2])
        if num_pages <= 0:
            raise ValueError("Number of pages must be a positive integer.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    try:
        trim_pdf(input_file, num_pages)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
