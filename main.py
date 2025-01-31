from scraper import Scraper

#scrape time!
scraper = Scraper()

#these methods all return one list
links = scraper.GetLinks()
titles = scraper.GetTitles()
dates = scraper.GetDates()
platforms = scraper.GetPlatforms()

# Get prices returns prices in dictionary that contains 3 lists
# List keys are 'prices_before', 'prices_final', 'discounts'
prices = scraper.GetPrices()
prices_before = prices.get('prices_before')
prices_after = prices.get('prices_final')
discounts = prices.get('discounts')

print()
