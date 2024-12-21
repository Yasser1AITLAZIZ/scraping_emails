from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Searcher:
    """
    A class to handle the search process using Selenium.
    """

    def __init__(self, query: str):
        """Initialize with a search query."""
        self.query = query
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def perform_search(self, site: str) -> List[str]:
        """Perform a search on the specified site and return a list of page HTMLs."""
        search_url = f"https://www.google.com/search?q={self.query}+site:{site}"
        self.driver.get(search_url)
        
        pages = []
        while True:
            pages.append(self.driver.page_source)
            try:
                next_button = self.driver.find_element(By.LINK_TEXT, "Next")
                next_button.click()
            except:
                break
        
        return pages

    def close(self):
        """Close the Selenium driver."""
        self.driver.quit()