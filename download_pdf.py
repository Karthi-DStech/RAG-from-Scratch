import os
import requests


class PDFDownloader:
    """
    Class to download PDF from a given URL

    Args:
    ------------
    pdf_path (str):
        Path to save the PDF file

    url (str):
        URL to download the PDF file

    Methods:
    ------------
    download_pdf:
        Downloads the PDF file from the given URL
    """

    def __init__(self, pdf_path: str, url: str):

        self._pdf_path = pdf_path
        self._url = url
        self._validate_path()
        self._validate_url()

    def _validate_path(self):
        """
        Validates the pdf_path to ensure it ends with '.pdf'

        Parameters:
        ------------
        None

        Raises:
        ------------
        ValueError:
            If the pdf_path does not end with '.pdf'
        """
        if not isinstance(self._pdf_path, str) or not self._pdf_path.endswith(".pdf"):
            raise ValueError("pdf_path should be a string ending with '.pdf'")

    def _validate_url(self):
        """
        Validates the URL to ensure it starts with 'http' or 'https'

        Parameters:
        ------------
        None

        Raises:
        ------------
        ValueError:
            If the URL does not start with 'http' or 'https'
        """
        if not isinstance(self._url, str) or not self._url.startswith("http"):
            raise ValueError("url should be a valid HTTP/HTTPS URL")

    def download_pdf(self):
        """
        Downloads the PDF file from the given URL

        Parameters:
        ------------
        None

        Returns:
        ------------
        Directories are created if they don't exist

        If the PDF file is downloaded successfully, it returns a message "File downloaded successfully!"

        It returns a message "Failed to download file! Status code: {response.status_code}"

        else if the file already exists, it returns a message "File already exists!":

        """
        directory = os.path.dirname(self._pdf_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        if not os.path.exists(self._pdf_path):
            print(f"File doesn't exist! Downloading PDF...")
            response = requests.get(self._url)

            if response.status_code == 200:
                with open(self._pdf_path, "wb") as file:
                    file.write(response.content)
                print("File downloaded successfully!")

            else:
                print(f"Failed to download file! Status code: {response.status_code}")

        else:
            print("File already exists!")

    @property
    def pdf_path(self):
        return self._pdf_path

    @property
    def url(self):
        return self._url


# TESTING THE CLASS
"""
if __name__ == "__main__":
    pdf_path = "../RAG-from-Scratch/human-nutrition-text.pdf"
    url = "https://pressbooks.oer.hawaii.edu/humannutrition2/open/download?type=pdf"
    downloader = PDFDownloader(pdf_path, url)
    downloader.download_pdf()

"""


