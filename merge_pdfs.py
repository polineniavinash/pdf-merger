import PyPDF2
import os

def merge_pdfs(pdf_files, output_path):
    """
    Merges multiple PDFs into a single PDF file.

    Parameters:
    - pdf_files: List of paths to PDF files to be merged.
    - output_path: Path to the output merged PDF file.
    """
    merger = PyPDF2.PdfMerger()

    for pdf in pdf_files:
        if not os.path.exists(pdf):
            print(f"Error: File '{pdf}' does not exist. Skipping.")
            continue

        try:
            with open(pdf, 'rb') as fileobj:
                merger.append(fileobj)
        except Exception as e:
            print(f"Error processing file '{pdf}': {e}")
            continue

    if merger.pages:
        try:
            with open(output_path, 'wb') as output_file:
                merger.write(output_file)
            print(f"Successfully merged PDFs into '{output_path}'")
        except Exception as e:
            print(f"Error writing output file '{output_path}': {e}")
        finally:
            merger.close()
    else:
        print("No PDFs were merged. Please check the input files.")

if __name__ == "__main__":
    # List the PDF files in the order you want them to appear in the merged PDF
    pdf_files = ['/Users/avinash/Desktop/merge-files/Page-1.pdf', '/Users/avinash/Desktop/merge-files/Page-2.pdf', '/Users/avinash/Desktop/merge-files/Page-3.pdf', '/Users/avinash/Desktop/merge-files/Page-4.pdf', '/Users/avinash/Desktop/merge-files/Page-5.pdf']

    # Output path for the merged PDF
    output_path = '/Users/avinash/Desktop/merge-files/merged_output.pdf'

    # Merge the PDFs
    merge_pdfs(pdf_files, output_path)