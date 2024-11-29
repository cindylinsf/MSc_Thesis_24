# November 11, 2024

**Notes & Updates:** 
Created sampling of both database for putting them through LLMs. Started to work on the thesis content. Created `sampled` folder for the results and analysis. 

During data augmentation process, the emphasis was placed on ethnicity/race of the donors, as well as an interest in education background. “Unknown” in ethnicity was disregarded.

**Key Actions:** Data sampling and start writing

What was done today:

1. Data Processing
- Successfully created augmented dataset with balanced ethnic distributions
- Original dataset: ~1,019 records
- Augmented dataset: ~1,014 records

2. Sampling Phase
- Created samples of 250 profiles from each dataset
- Implemented marketing pattern analysis
- Generated comprehensive analysis report

Key Marketing Patterns Found (Original vs Augmented):
- Physical descriptions (facial features): 205 vs 188 mentions
- Personality (altruism): 203 vs 154 mentions
- Professional achievements: 202 vs 193 mentions
- Athletic descriptions: 179 vs 168 mentions
- Intelligence emphasis: 142 vs 94 mentions

Notable Differences:
- Original dataset shows strong preferences for certain traits
- Augmented dataset shows more balanced distribution
- Clear patterns of potential bias in marketing narratives

Current Stage:
Preparing for LLM testing phase using:
- ChatGPT
- Gemini
- Llama-3

Next Steps:
Generate new donor profiles using these LLMs:
- 25 profiles per LLM from original sample (75 total)
- 25 profiles per LLM from augmented sample (75 total)