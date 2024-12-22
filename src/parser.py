import re
from bs4 import BeautifulSoup
import logging

class Parser:
    """
    A class to parse HTML pages and extract email addresses.
    """

    @staticmethod
    def extract_emails(page_html: str) -> set:
        """
        Extract emails from a single HTML page.
        """
        try:
            soup = BeautifulSoup(page_html, "html.parser")
            text = soup.get_text()
            emails = set(re.findall(r'[a-zA-Z0-9_.+-]+@gmail\\.com', text))
            return emails
        except Exception as e:
            logging.exception("Error occurred while extracting emails.")
            return set()
