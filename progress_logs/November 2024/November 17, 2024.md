# November 17, 2024

**Notes & Updates:** 
✅ Llama finetuning: had to switch to Google Colab because of CUDA/CPU/MPS conflicts. Also changed Llama model to OPT-1.3B due to memory usage issue
✅ Start thesis draft


**Key Actions:** Llama finetuning, mostly debugging, which is super frustrating and I am now really worried about finishing on time.

### Data Processing for Tokenization
- The processing maintained all original data
- The format follows a clear instruction-response pattern
- Preserved the marketing-style narratives
- The data is now structured for instruction fine-tuning

### Training issues using my Macbook
- I couldn’t debug issues with mps vs. cuda in the training step, so I moved the rest of the notebook onto Google Drive and Google Colab
- Here is the folder structure on Google Drive (mimicking what I have on my Macbook)

Thesis_Llama_Training/ (in Google Drive)
├── data/
│   ├── sampled/                      # Original data files from Macbook
│   │   ├── original_sample.json
│   │   └── augmented_sample.json
│   └── processed/                    # Only intermediate processing results
│       └── llama_training/           # Processed datasets ready for training
│           ├── processed_original_dataset.json
│           └── processed_augmented_dataset.json
├── outputs/                          # All training outputs
│   └── llama_fine_tuned/
│       ├── checkpoints/              # Training checkpoints
│       ├── logs/                     # Training logs
│       └── final_model/              # Final trained model
└── notebooks/
└── llama_training.ipynb