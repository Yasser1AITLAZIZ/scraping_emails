from typing import List
from searcher import Searcher
from csvhandler import CSVHandler
from parser import Parser


class Bot:
    """
    The main bot to orchestrate the search, parse, and save process.
    """

    def __init__(self, query: str, sites: List[str], output_file: str):
        self.query = query
        self.sites = sites
        self.csv_handler = CSVHandler(output_file)

    def run(self):
        """Run the bot."""
        searcher = Searcher(self.query)

        try:
            for site in self.sites:
                print(f"Searching on {site}...")
                pages = searcher.perform_search(site)

                for page_html in pages:
                    emails = Parser.extract_emails(page_html)
                    self.csv_handler.save_emails(emails)

        finally:
            searcher.close()