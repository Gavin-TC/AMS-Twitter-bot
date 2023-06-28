# American-Mass-Shootings Twitter Bot
This is a Twitter bot that tweets about a mass shooting in the United States. It usually posts it quite a bit after it took place because gunviolencearchive.org (where the information is taken from) updates their database shortly after the event occurred.

# What it does 
This bot has a webscraper that clicks a couple button to download the CSV file provided by the gunviolencearchive.org website every 15 minutes.
After a new CSV is downloaded it is compared to the last CSV it had (the 'old' one) and checks if the 'new' one has more entries.
If this is the case, it takes all that data and tweets it. It deletes the 'old' CSV and the 'new' CSV becomes the 'old' one.
