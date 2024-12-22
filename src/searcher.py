from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
import undetected_chromedriver as uc
import logging
import time
import os

class Searcher:
    """
    A class to handle the search process using Selenium.
    """

    def __init__(self, query: str, logger: logging.Logger):
        self.query = query
        self.logger = logger
        self.driver = None
        self.setup_driver()

    def setup_driver(self) -> None:
        """
        Configures the browser for scraping using undetected-chromedriver and webdriver_manager.
        This ensures the correct ChromeDriver version is selected automatically.
        """
        self.logger.info("Setting up the Chrome driver with undetected-chromedriver and webdriver_manager.")

        options = uc.ChromeOptions()
        # Run in headless mode in server environments
        options.headless = False
        options.add_argument("--window-size=1920x1080")
        user_agent = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        )
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("--lang=fr-FR")
        options.add_argument('--incognito')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')

        try:
            # Use webdriver_manager to automatically install the correct driver
            driver_path = ChromeDriverManager().install()
            self.driver = uc.Chrome(options=options, driver_executable_path=driver_path)
            self.logger.info("Chrome driver setup complete with webdriver_manager.")
        except WebDriverException as e:
            self.logger.error(f"Error initializing Chrome driver: {e}")
            raise

    def perform_search(self, site: str) -> list:
        """
        Perform a search on the specified site and return a list of page HTMLs.
        """
        try:
            search_url = f"https://www.google.com/search?q={self.query}+site:{site}"
            self.logger.info("Performing search for: %s", search_url)
            self.driver.get(search_url)
            time.sleep(5)
            self.save_page_source(f"page_content_{site}.html")

            pages = []
            while True:
                pages.append(self.driver.page_source)
                try:
                    next_button = self.driver.find_element(By.LINK_TEXT, "Next")
                    next_button.click()
                    self.logger.info("Navigating to the next page.")
                except Exception as e:
                    self.logger.info("No more pages to navigate.")
                    break

            return pages
        except Exception as e:
            self.logger.exception("Error occurred during search.")
            raise

    def close(self):
        """
        Close the Selenium driver.
        """
        try:
            self.driver.quit()
            self.logger.info("Selenium driver closed.")
        except Exception as e:
            self.logger.exception("Error occurred while closing the driver.")
            
    def save_page_source(self, file_name: str) -> None:
        """
        Saves the current page source to a file for debugging purposes.

        Args:
            file_name (str): Name of the file where the page source will be saved.
        """
        try:
            page_source = self.driver.page_source
            os.makedirs(os.path.dirname("./data_brute/"), exist_ok=True)
            with open("./data_brute/"+ file_name, "w", encoding="utf-8") as file:
                file.write(page_source)
            self.logger.info(f"Page source saved to {file_name} for debugging.")
        except Exception as e:
            self.logger.error(f"Failed to save page source: {e}")            
