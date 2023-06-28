# American-Mass-Shootings
This is a twitter bot that tweets when a mass shooting occurs in the United States.

# What it does 
This bot has a webscraper that clicks a couple button to download the CSV file provided by the gunviolencearchive.org website every 15 minutes.
After a new CSV is downloaded it is compared to the last CSV it had (the 'old' one) and checks if the 'new' one has more entries.
If this is the case, it takes all that data and tweets it. It deletes the 'old' CSV and the 'new' CSV becomes the 'old' one.
