# November 16, 2024

**Notes & Updates:** 
✅ After reading about different models, decided to work with Llama 2 7bhf
✅ Installed new conda llama_thesis for the finetuning
✅ Get permissions from Meta to use Llama 2

**Key Actions:** Working on Llama finetuning

Model via HuggingFace: https://huggingface.co/meta-llama/Llama-2-7b-hf

# LoRA (Low-Rank Adaptation)
LoRA Advantages:
1. Memory Efficient
    - Instead of fine-tuning all model parameters, LoRA updates a small number of adaptation parameters
    - Since I have limited GPU memory, this allows me to work with larger base models on a Macbook
2. Training Speed
    - Faster training times compared to full fine-tuning
    - Requires less computational resources
3. More Manageable
    - LoRA creates lightweight "adaptations" of larger models
    - LoRA works by identifying and modifying key parameters that have the most impact
    - LoRA process involves reducing complex systems to manageable, influential components
    - This raises questions about what information is deemed "essential" vs. "peripheral"

## Possible discussion Qs:
- Data reduction choices
- Information preservation
- Optimization vs. diversity
- Technical constraints

## Current Methodology:
- I have two datasets (Original Sampled and Augmented Sampled)
- I used the same prompts across Claude, ChatGPT, and Gemini
- I interacted with them through their standard interfaces, which represents how the general public would access these tools
1. For Llama 2 Comparison:
- We should maintain similar input/output structures
- The fine-tuned model should accept similar prompts
- The output format should be comparable

Will:
- Structure the LoRA fine-tuning appropriately
- Design the right prompt template
- Ensure the outputs are comparable
- Set up proper evaluation metrics

The key difference here will be that instead of using a web interface, I'll be:
1. Fine-tuning Llama 2 on the two datasets
2. Creating a simple interface to input the same prompts
3. Generating outputs that can be directly compared with existing results

This approach will allow me to compare:
- Standard prompt engineering (my existing results)
- Fine-tuned model outputs (Llama 2)

The fine-tuning pipeline:
1. Data Preprocessing:
- Convert JSON data into instruction-following format
- Structure prompt-completion pairs
- Handle any null values consistently
- Ensure consistent formatting

2. Fine-tuning Setup:
- Use Llama 2 7B as base model (size appropriate for M3)
- Implement LoRA for efficient training
- Set up validation splits to monitor training

3. Training Strategy:
- Train two separate versions:
a. One on Original dataset
b. One on Augmented dataset
- This maintains the parallel with existing methodology

4. Evaluation Plan:
- Generate 10 profiles from each fine-tuned version
- Compare with Claude/ChatGPT/Gemini outputs
- Analyze consistency and bias patterns