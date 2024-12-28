from searcher import Searcher
from parser import Parser
from csvhandler import CSVHandler
import logging

class Bot:
    """
    The main bot to orchestrate the search, parse, and save process.
    """

    def __init__(self, url: str, output_file: str, logger: logging.Logger):
        self.url = url
        self.csv_handler = CSVHandler(output_file)
        self.logger = logger

    def run(self):
        """
        Run the bot.
        """
        searcher = Searcher(self.logger)

        try:
            searcher.perform_search(self.url)

        except Exception as e:
            self.logger.exception("An error occurred during the bot execution.")
        finally:
            searcher.close()
            self.logger.info("Bot execution completed.")