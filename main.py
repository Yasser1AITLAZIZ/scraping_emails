from bot import Bot


# Configuration
QUERY = '"Influencer" "micro influencer"+"ID" "@gmail.com" -intitle:"profiles" -inurl:"dir/ "'
SITES = ["www.instagram.com", "www.facebook.com"]
OUTPUT_FILE = "emails.csv"

# Run the bot
bot = Bot(QUERY, SITES, OUTPUT_FILE)
bot.run()