# October 30, 2024

**Notes & Updates:** Debugging bank3.

I ended up taking a simpler approach and only focusing on scraping information that I can get without logging in. This simplifies the process a lot where instead of spending hours trying to login and dealing with timeout issues or the platform's anti-scraping measures, I just need to: 

- mimic human behaviors and deal with pagination
- scrape all the donor IDs
- using the set URL structure to go to the donor profile and using the right html structure to scrape

**Key Action:** Continue with web scraping