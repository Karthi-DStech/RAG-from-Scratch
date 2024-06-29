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
    def __init__(self, pdf_path, url):
        self.pdf_path = pdf_path
        self.url = url

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
        directory = os.path.dirname(self.pdf_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        if not os.path.exists(self.pdf_path):
            print(f"File doesn't exist! Downloading PDF...")
            response = requests.get(self.url)
            
            if response.status_code == 200:
                with open(self.pdf_path, 'wb') as file:
                    file.write(response.content)
                print("File downloaded successfully!")
                
            else:
                print(f"Failed to download file! Status code: {response.status_code}")
                
        else:
            print("File already exists!")



# TESTING THE CLASS

"""
Example:
--------

if __name__ == "__main__":
    pdf_path = "../cd/human-nutrition-text.pdf"
    url = "https://pressbooks.oer.hawaii.edu/humannutrition2/open/download?type=pdf"
    downloader = PDFDownloader(pdf_path, url)
    downloader.download_pdf()      
"""


    
    
    
