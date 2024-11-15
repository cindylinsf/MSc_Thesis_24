# October 16, 2024

**Notes & Updates:** 
✅ Set up file structure
✅ Set up conda enviornment

**Key Action:** Building web scrapers and data structure

### Set up Conda

1. Environment name: `msc_thesis_24` python=3.9
2. Installed required packages: `requests` `beautifulsoup4` `pandas` `jupyter`

### File Structure

- MSc_Thesis_Project
    - **data** (for all data files)
        - **raw** (unprocessed data scraped from each sperm bank)
        - **processed** (cleaned and standardized data files)
        - **generated** (files related to the AI-generated donors, including images, etc.)
    - **scrapers** (all the web scraping scripts, with each sperm bank having its own script)
    - **models** (any trained machine learning models created for generating donor descriptions or images)
    - **outputs** (all the final outputs of the project, like photographic prints, videos, and audio files)
    - **notebooks** (all the Jupyter notebooks for analysis or model training)
    - **readme.md** (A markdown file explaining your project, the structure of the directories, and instructions for running the scrapers or models.)

