# November 19, 2024

**Notes & Updates:** 
A/B testing with and without demographic information to compare results and observe any bias


**Key Actions:** 
✅ Did the bulk of donor profile image generation and database creation for tracking all the image generations
✅ Created json2csv.ipynb to convert existing generated profiles by LLMs database llm_generated_profile.json into .csv format. Results from Llama are not included here because the generations were not successful for comparison. 

It was really labor intensive to generate donor images one by one, despite the illusion that we are simply feeding a prompt into an interface. It reminds me of Christov-Bakergiev’s essay criticizing how AI have enslaved us: https://www.castellodirivoli.org/en/hito-steyerl-they-are-oblivious-to-the-violence-of-their-acts-windows-screens-and-pictorial-gestures-in-troubled-times/#_ftnref1

### Methodology

1. **Systematic Generation:**
    - Same prompt structure
    - Same order of information
    - No additional styling instructions
    - No modifications between models
2. This will allow me to observe:
    - How different AI models interpret the exact same text
    - How adding demographics influences interpretation
    - Whether certain models show more or less bias with identical inputs
    - Consistency issues between models given the same prompt

## For Text-to-Image Generation:

### Commercial/Public Models (Baseline):

- Keep these to demonstrate "public access" bias:
    - Midjourney
    - DALL-E
    - Gemini Imagen 3

### Fine-tunable Models:

- Stable Diffusion (key choice because):
    - Highly customizable
    - Can be fine-tuned with different techniques
    - Open source, allowing deeper analysis of bias sources
    - Good documentation of my process for academic purposes

### Testing Strategy:

1. Run A/B tests (with/without demographics) through both:
    - Commercial models (showing current public-facing bias)
    - Fine-tuned models (showing potential for bias mitigation/amplification)
2. For fine-tuning experiments:
    - Fine-tune with original dataset → generate images
    - Fine-tune with augmented dataset → generate images
    - Compare how the balance/imbalance in training data affects output
    - This directly parallels my text generation methodology

This approach would create an interesting parallel between:

- Text generation (Claude, ChatGPT, Gemini) vs. Image generation
- Public vs. Fine-tuned models
- Original vs. Augmented dataset impacts

1. **Thread Management:**
- Yes, absolutely **start new threads for each generation**. This will:
    - Keep results clean and traceable
    - Avoid any context contamination
    - Make documentation and comparison easier
    - Help isolate any biases or patterns specific to each model
1. A/B Testing Volume:
Let's break down the numbers:
- 60 total donor profiles = (3 LLMs × 2 datasets × 10 profiles each)
- Running each through 3 image models (Gemini, Midjourney, DALL-E)
- With both demographic/non-demographic versions

This would mean:
60 profiles × 2 versions × 2 image models = 240 generated images

Look at:

1. How dataset bias affects model outputs
2. Whether balanced training data produces more equitable results
3. The relationship between text generation bias and image generation bias

# Prompt for Text-to-image model

Yes, absolutely use the same prompt structure for consistency! Let me help break this down:

## **Prompt Structures:**

```
**[Without Demographics Version]**
Create a photorealistic passport-style portrait of a sperm donor with the following characteristics: [description_from_profile]. The image should be a front-facing headshot with neutral background, neutral expression, and clear lighting, similar to a passport photo or ID photograph.
```

```
**[With Demographics Version]**
"Create a photorealistic passport-style portrait of a sperm donor with the following characteristics: [description_from_profile_with_demo_info]. The image should be a front-facing headshot with neutral background, neutral expression, and clear lighting, similar to a passport photo or ID photograph."
```

### Naming Convention for Generated Images

```
Naming convention:
**[profile_id]_[text-to-image-model]_[demo/nodemo].jpg**

Examples:
cla_org_01_gem_demo.jpg // org_cla_1_gem_wo.jpeg

Code:
LLM: cla/gpt/gem
Text to Image Models: gem/mid/dal
Demo: demo/wo
```

## Analysis Approach:

### Visual Database in Airtable:

- Main Table Structure:
    - Profile Code (my existing system)
    - Original Text Description
    - Demographic Info
    - Generated Images (both versions)
    - Analysis Fields:
        - Perceived ethnicity
        - Key physical features
        - Consistency with description
        - Bias indicators
        - Notable differences between demo/no-demo versions

### Analysis Categories:

- Text vs. Image Correlation
- Demographic Impact
- Cross-Model Consistency
- Dataset Influence (Original vs. Augmented)
- Bias Patterns

## Rationale to remove fine-tuning

Given the project's focus on how AI bias impacts human decisions in fertility choices, I think the current methodology (comparing commercial models with both demographic and non-demographic prompts) is actually stronger for the argument. It shows real-world impact using tools actually available to fertility marketers and consumers.

Instead of fine-tuning, I might want to focus on:

1. Thorough analysis of the 360 generated images
2. Documentation of found biases
3. Implications for fertility marketing
4. Impact on personal decision-making

**Technical Complexity Already Present:**

1. Multi-Stage AI Implementation:
    - Text generation using 3 different LLMs
    - Dataset augmentation and balance analysis
    - Systematic image generation across 3 different models
    - Offspring generation with fine-tuning (this is a significant technical element!)
2. Methodological Rigor:
    - Controlled A/B testing
    - Large-scale systematic comparison (360 images)
    - Cross-model analysis
    - Multiple data transformations
3. Novel Technical Approaches:
    - Using AI to simulate genetic inheritance
    - Comparing augmented vs. original datasets
    - Multi-model bias analysis
    - Combining text and image generation

Offspring Generation Plans:

- Fine-tuning for genetic feature inheritance is much more relevant to my thesis
- Shows direct impact on personal decision-making
- Creates powerful visual evidence of AI bias