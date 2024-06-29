import fitz
from tqdm.auto import tqdm
import re

from download_pdf import PDFDownloader
import random


class PDFProcessor:
    """
    Class to process PDF files by extracting and preprocessing text from each page.

    Methods:
    ------------
    _text_formatter:
        Preprocesses the text by replacing newline characters and stripping whitespace.
    open_and_read_pdf:
        Opens a PDF file and extracts text from each page.
    process_pdf:
        Processes the PDF and returns the information of the specified number of pages
    """

    def __init__(self, pdf_path: str, page_offset: int):
        self.pdf_path = pdf_path
        self._page_offset = page_offset

    def _text_formatter(self, text: str) -> str:
        """
        Function to preprocess text by performing the following operations:
        - Replace newline characters with spaces
        - Strip leading and trailing whitespace
        - Reduce multiple spaces to a single space

        Args:
        ------------
        text (str): The text to be preprocessed

        Returns:
        ------------
        str: The preprocessed text
        """
        # Replace newline characters with spaces
        cleaned_text = text.replace("\n", " ")

        # Strip leading and trailing whitespace
        cleaned_text = cleaned_text.strip()

        # Reduce multiple spaces to a single space
        cleaned_text = re.sub(r"\s+", " ", cleaned_text)

        return cleaned_text

    def open_and_read_pdf(self) -> list[dict]:
        """
        Function to open and read a PDF file, extracting and preprocessing text from each page.

        Args:
        ------------
        None

        Returns:
        ------------
        list[dict]: A list of dictionaries containing page information and text
        """
        try:
            doc = fitz.open(self.pdf_path)
        except Exception as e:
            raise ValueError(f"Could not open PDF file: {e}")

        pages_and_text = []

        for page_number, page in tqdm(enumerate(doc), total=len(doc)):

            text = page.get_text()

            text = self._text_formatter(text=text)

            word_count = len(text.split(" "))

            sentence_count = text.count(".")

            token_count = len(text.split(" "))

            pages_and_text.append(
                {
                    "page_number": page_number - self._page_offset,
                    "page_character_count": len(text),
                    "page_word_count": word_count,
                    "page_sentence_count": sentence_count,
                    "page_token_count": token_count,
                    "text": text,
                }
            )

        return pages_and_text

    def process_pdf(self, num_pages: int) -> list[dict]:
        """
        Function to process the PDF and return the information of the specified number of pages

        Args:
        ------------
        num_pages (int): Number of pages to return information for

        Returns:
        ------------
        list[dict]: A list of dictionaries containing page information and text for the specified number of pages
        """
        pages_and_text = self.open_and_read_pdf()
        return pages_and_text[:num_pages]

    def sample_pages(self, k: int) -> list[dict]:
        """
        Function to return a random sample of the processed pages

        Args:
        ------------
        k (int): Number of pages to sample

        Returns:
        ------------
        list[dict]: A random sample of dictionaries containing page information and text
        """
        pages_and_text = self.open_and_read_pdf()
        return random.sample(pages_and_text, k)


"""

def run():

    # Download the PDF
    pdf_path = "../RAG-from-Scratch/human-nutrition-text.pdf"
    url = "https://pressbooks.oer.hawaii.edu/humannutrition2/open/download?type=pdf"
    downloader = PDFDownloader(pdf_path, url)
    downloader.download_pdf()

    # Process the PDF
    processor = PDFProcessor(pdf_path, page_offset=41)
    pages_and_text = processor.process_pdf(num_pages=2)

    # Print the information of the specified pages
    for page_info in pages_and_text:
        print(page_info)


if __name__ == "__main__":
    run()

"""

"""
def run():

    # Download the PDF
    pdf_path = "../RAG-from-Scratch/human-nutrition-text.pdf"
    url = "https://pressbooks.oer.hawaii.edu/humannutrition2/open/download?type=pdf"
    downloader = PDFDownloader(pdf_path, url)
    downloader.download_pdf()

    # Process the PDF and sample pages
    processor = PDFProcessor(pdf_path, page_offset=41)
    sampled_pages = processor.sample_pages(k=3)

    # Print the information of the sampled pages
    for page_info in sampled_pages:
        print(page_info)


if __name__ == "__main__":
    run()
"""
