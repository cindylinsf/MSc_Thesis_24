# October 23, 2024

**Notes & Updates** For more details on this entry, please refer to the progress_logs folder.
Key Action: Editing and debugging files to anonymize sensitive data from being committed to Github repository.

Coding is like whack-a-mole. Just when I thought something was resolved, a new issue pops up 😵

**Today’s goals:****
~~☠️ Wrap bank2 scraper~~
~~☠️ Set up GitHub repo~~
☠️ Debug bank1 scraper

**What I actually did:**
✅ bank2 scraper is now fully functioning with its accompanying documents `login.py`, `config.json`, `config.py`, `log_utils.py`
✅ Added additional helper functions to anonymize the outputs
✅ raw data for bank2 is almost complete
✅ Started the process of syncing Notion work log to Github repo
✅ Killed original repo because after seeing the output, I realized all the data I spent hours to debug in order to anoymize the process and hide are showing up in the cell output printouts. Added new document `log_utils.py` to anonymize all the output
✅ Set up new repo 
✅ Deciding key fields to focus on scraping

1. Physical Characteristics (for both text and image generation):
    ◦ Race/Ethnicity
    ◦ Skin tone
    ◦ Eye color
    ◦ Hair color
    ◦ Height
    ◦ Build/Weight
2. Descriptive Text (for LLM analysis):
    ◦ Donor descriptions/personal statements
    ◦ Personality descriptions
    ◦ Background narrative
3. Demographic Information:
    ◦ Education level
    ◦ Occupation
    ◦ Nationality
    ◦ Languages spoken
4. Cultural Indicators:
    ◦ Religion
    ◦ Interests/Hobbies
    ◦ Skills