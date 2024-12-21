import re
from typing import Set
from bs4 import BeautifulSoup


class Parser:
    """
    A class to parse HTML pages and extract email addresses.
    """

    @staticmethod
    def extract_emails(page_html: str) -> Set[str]:
        """Extract emails from a single HTML page."""
        soup = BeautifulSoup(page_html, "html.parser")
        text = soup.get_text()
        return set(re.findall(r'[a-zA-Z0-9_.+-]+@gmail\.com', text))