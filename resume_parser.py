import pypdf

def read_pdf(file_path):
    try:
        # Open the PDF file in read-binary mode, to read the contents
        with open(file_path, 'rb') as file:
            # Create a PDF reader object
            pdf_reader = pypdf.PdfReader(file)
            
            # Get the total number of pages
            num_pages = len(pdf_reader.pages)
            print(f"Total Pages: {num_pages}\n" + "-"*30)
            
            # Loop through all the pages and extract text
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                
                print(f"--- Page {page_num + 1} ---")
                print(text)
                print("\n")
                
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# Replace 'example.pdf' with the path to your actual PDF file. The lcoation of your file.
def main():
    read_pdf('Documents\Resume_v3.pdf')

