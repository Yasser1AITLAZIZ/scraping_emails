from searcher import Searcher
from parser import Parser
from csvhandler import CSVHandler
import logging

class Bot:
    """
    The main bot to orchestrate the search, parse, and save process.
    """

    def __init__(self, query: str, sites: list, output_file: str, logger: logging.Logger):
        self.query = query
        self.sites = sites
        self.csv_handler = CSVHandler(output_file)
        self.logger = logger

    def run(self):
        """
        Run the bot.
        """
        self.logger.info("Bot initialized with query: %s", self.query)
        searcher = Searcher(self.query, self.logger)

        try:
            for site in self.sites:
                self.logger.info("Searching on site: %s", site)
                pages = searcher.perform_search(site)

                for i, page_html in enumerate(pages, start=1):
                    self.logger.info("Parsing page %d for site %s", i, site)
                    emails = Parser.extract_emails(page_html)
                    self.logger.info("Extracted %d emails from page %d", len(emails), i)
                    self.csv_handler.save_emails(emails)

        except Exception as e:
            self.logger.exception("An error occurred during the bot execution.")
        finally:
            searcher.close()
            self.logger.info("Bot execution completed.")