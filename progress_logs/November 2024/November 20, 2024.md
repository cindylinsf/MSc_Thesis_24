# November 20, 2024

**Notes & Updates:** 
Airtable database with all the generated donor images: https://airtable.com/appg1vFKTmJbbQkKR/shrjPTsv4bt5SJwCZ

**Key Actions:**
✅ Finished 240 donor profile image generations! (only took 7 hours)
✅ Generating offspring photos with ComfyUI


Gemini seems to have stronger "ethical" filters that trigger when demographic information is explicitly provided, while generating similar images without issue when demographic information is removed.

# ComfyUI

Let me explain ComfyUI and JSON workflows:

ComfyUI works like a visual programming interface where different "nodes" (components) connect together to create an image generation pipeline. Each node performs a specific function, like:

- Loading images
- Processing images
- Applying AI models
- Setting parameters
- Saving outputs

A JSON workflow is essentially a "recipe" or "blueprint" that contains:

1. All the nodes we need
2. How they're connected
3. All their settings and parameters

Think of it like sharing a Photoshop action or a Premiere Pro preset - instead of manually recreating the workflow, we can import it and have everything set up automatically.

For specific aesthetic goals >> workflow:

1. **Input Processing Nodes**
    - Load Images: my photo and donor photos
    - Face Detection: To properly identify and preserve facial features
    - Background Removal: To ensure consistent neutral background
2. **Age and Style Control Nodes**
    - Age Conditioning: To ensure consistent baby-like features (around 12 months)
    - Lighting Control: To achieve soft, even lighting like the reference
    - Expression Control: For the gentle smile
3. **Feature Blending Nodes**
    - IP-Adapter: To intelligently blend facial features from both parents
    - ControlNet Face: To maintain realistic baby facial structure
    - Feature Weight Control: To balance genetic features
4. **Output Refinement Nodes**
    - Background Generation: To create the cream/beige backdrop
    - Final Cleanup: To ensure consistent quality
    - Image Saving: To follow our naming convention
