# MSc Thesis Project Delivery
In this repository, you will find most of the files used in the creation of this thesis project. Certain files have been omitted to protect the anonymity of the scraped data sources, which are included in the `.gitignore` file.

# Project File Structure
- `data`/: Main directory containing all data-related files and subdirectories
    - `/data_llama_finetuning`: Contains llama model fine-tuning data and related files
     - `/generated`: Contains generated augmented dataset
    - `/input`: Input data directory
    - `/processed`: Contains processed datasets for training
    - `/sampled`: Contains sampled datasets
    - `/raw` Raw data directory is intentionally excluded to protect the anonymity of the sperm banks from which the dataset was obtained.
- `models`/: Only the interpolation workflow files are included, as the model repositories used in this project are too large to upload to GitHub.
- `notebooks`/: Jupyter notebooks used in ComfyUI offspring generations, data augmentations and sampling, Llama finetuning and frame interpolation
- `outputs`/: Output files and results. 
    - Video files are excluded due to Github upload size limitation. Final video output links are listed below.
- `progress_logs`/: Contains journal entries documenting progress reports organized by month.
- `scrapers`/: Web scraping scripts

# Project Outputs:
- _Baby Lottery_ video link: https://vimeo.com/1034183475?share=copy
- _All My Children_ video link: https://vimeo.com/1034183933?share=copy 
- Oral project report video link: https://vimeo.com/1034516433?share=copy 

# Written Thesis:
- Included in the submission zip folder

# A weblog 
- Daily entries (in `.md` format) documentating iterative development is included in the `progress_logs` organized by month. 
- A PDF is converted from the `.md` format entries, which is included in the zipped folder. Please note that the format may have changed during the conversion process.

# LLM Disclosure
This thesis and project utilized language models to assist in coding and generative outputs. The use of LLMs in this project contributed to the development of various components, such as developing and refining python scripts for web scraping, generating donor descriptions and images. 