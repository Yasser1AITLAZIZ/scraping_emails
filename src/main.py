import os
from bot import Bot
from logger import setup_logger

# Set up logging
logger = setup_logger("EmailScraper", "logs/email_scraper.log")

def main():
    """
    Main function to execute the email scraping bot.
    """
    QUERY = '"Influencer" "micro influencer"+"ID" "@gmail.com" -intitle:"profiles" -inurl:"dir/ "'
    SITES = ["www.instagram.com", "www.facebook.com"]
    os.makedirs(os.path.dirname("data_brute/"), exist_ok=True)
    OUTPUT_FILE = "data_brute/emails.csv"

    logger.info("Starting Email Scraper Bot...")
    try:
        bot = Bot(QUERY, SITES, OUTPUT_FILE, logger)
        bot.run()
    except Exception as e:
        logger.exception("An error occurred during execution.")
    finally:
        logger.info("Email Scraper Bot execution finished.")

if __name__ == "__main__":
    main()
