# November 21, 2024

**Key Actions:** Continue with ComfyUI debugging

About sampling parameters:
    - Sampling Steps: Number of iterations to refine the image. Higher steps = more detail but longer generation time
        - For SDXL Turbo, 20-30 steps usually gives good results
        - Above 50 steps often gives diminishing returns
    - CFG (Classifier Free Guidance): Controls how closely the generation follows prompt
        - Lower values (4-7): More creative/diverse results
        - Higher values (8-12): More literal interpretation
        - Maybe keeping it moderate (around 7) to see the model's natural tendencies?

KSampler is a key component in Stable Diffusion workflows that controls how the AI generates images. Let me break down its main parameters:

1. Steps (we're using 25):
    - Think of it like iterations of refinement
    - Higher steps = more refined details but slower generation
    - Lower steps = faster but possibly less detailed
2. CFG (Classifier Free Guidance) (we're using 7.0):
    - Controls how closely the AI follows the prompt
    - Like a "creativity vs accuracy" slider
    - Lower values (1-5): More creative/diverse results
    - Higher values (8+): More literal interpretation of prompt
    - 7.0 is a balanced value that allows some natural variation while maintaining quality
3. Sampler (we're using "euler"):
    - Different mathematical methods for generating the image
    - "euler" is reliable and produces good results
    - Other options include: ddim, dpm++, etc.
    - Each has slightly different characteristics
4. Seed:
    - Like a starting point for the generation
    - Same seed + same parameters = same image
    - Random seed = new variation each time
    - Useful for reproducing specific results

- KSampler is where potential biases might manifest
- We're using moderate values to let the AI operate relatively naturally


In the beginning, the baby portrait looks more like an illustration, so I bumped up CFG (for stronger adherence to photorealism) and steps (for more detail refinement)

Here's the difference between Euler and Euler Ancestral samplers:

Euler:

- More stable and consistent results
- Better at preserving specific details
- Less random variation between generations
- Good for predictable, controlled results
- Often used for portrait-style images where stability is important

Euler Ancestral:

- Adds controlled randomness to the sampling process
- Can produce more natural-looking details and textures
- Better at generating organic-looking features
- Might produce more photorealistic results, but with more variation
- Good for natural textures like skin, hair, fabric


- steps (currently 25) -> Change this to 35
- cfg (currently 7.0) -> Change this to 8.5

Negative prompt: "blurry, distorted, bad quality, deformed, illustration, cartoon, drawing, painting, anime, 3d render, digital art, sketch, artificial, unrealistic, doll-like, fake-looking, oversaturated”

![Screenshot 2024-11-21 at 4.00.59 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7fa0be16-4a50-4137-a290-17d008668d2e/661fd534-6a03-4f1d-9f88-9df972fbb02f/Screenshot_2024-11-21_at_4.00.59_PM.png)

Positive prompt: raw photograph of a 12 month old baby, front portrait, natural lighting, natural skin pores and texture, photographic, unedited, candid baby photo, authentic, 50mm lens, pure photography, human baby, real skin texture, pores visible, subsurface scattering, studio lighting, white background, passport photo style, DSLR, 8k, hyper realistic

Negative prompt: illustration, drawing, digital art, CGI, 3d render, cartoon, anime, smooth plastic skin, artificial, doll-like, airbrushed, vector art, flat colors, oversaturated, painting style, concept art, unnatural lighting, artificial smoothing, digital painting, Pixar, Disney, dream-like, graphics, video game

- Increase CFG to 9.0 (for stronger adherence to photorealism)
- Increase steps to 40 (for more detail refinement)

![Screenshot 2024-11-21 at 4.04.16 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7fa0be16-4a50-4137-a290-17d008668d2e/99743dc3-3ead-4884-838e-fead120d2cb5/Screenshot_2024-11-21_at_4.04.16_PM.png)

positive prompt: professional passport photo of a healthy 12 month old baby, front facing portrait, clean natural lighting, clear face, soft natural skin, white background, sharp focus, high quality photograph, Canon camera, photorealistic, no editing, neutral expression

negative prompt: distorted, deformed, ugly, mutation, blurry, grainy, noisy, oversaturated, overprocessed, artificial, harsh lighting, unrealistic colors, plastic skin, extreme contrast, overexposed, surreal, watercolor, painting, illustration, artificial HDR, oversharpened

1. Adjust KSampler parameters:
- Steps: 30 (we went too high with 40)
- CFG: 7.5 (bring it down from 9.0 to reduce over-processing)
- Denoise: 0.8 (instead of 1.0 to preserve some natural qualities)

![Screenshot 2024-11-21 at 4.09.30 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7fa0be16-4a50-4137-a290-17d008668d2e/0537fa0d-825d-40c0-88a8-58ec3b55e3f8/Screenshot_2024-11-21_at_4.09.30_PM.png)

When I switched to `euler_ancestral` setting, it was not much better.

![Screenshot 2024-11-21 at 4.21.45 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7fa0be16-4a50-4137-a290-17d008668d2e/19821632-9153-46e0-9a02-f9f2d7aef87c/Screenshot_2024-11-21_at_4.21.45_PM.png)

### Successful Configuration:

1. Positive Prompt (CLIPTextEncode 4):

```
professional passport photo of a healthy 12 month old baby, front facing portrait, clean natural lighting, clear face, soft natural skin, white background, sharp focus, high quality photograph, Canon camera, photorealistic, no editing, neutral expression

```

1. Negative Prompt (CLIPTextEncode 9):

```
distorted, deformed, ugly, mutation, blurry, grainy, noisy, oversaturated, overprocessed, artificial, harsh lighting, unrealistic colors, plastic skin, extreme contrast, overexposed, surreal, watercolor, painting, illustration, artificial HDR, oversharpened

```

1. KSampler Parameters:
- Steps: 30
- CFG: 7.5
- Sampler: euler (about to change to euler_ancestral)
- Scheduler: normal
- Denoise: 0.8
1. Image Settings:
- Size: 512 x 512 (from EmptyLatentImage node)



1. Prompting Parameters:
    - Positive Prompt: Acts as instructions for desired features
        - "professional passport photo" - sets formal, standardized style
        - "healthy 12 month old baby" - specifies age and condition
        - "front facing portrait" - ensures consistent pose
        - "clean natural lighting" - controls for lighting variables
        - "photorealistic" - pushes toward real photography
    - Negative Prompt: Guards against unwanted characteristics
        - "distorted, deformed" - prevents anatomical errors
        - "artificial, plastic skin" - prevents unrealistic textures
        - "painting, illustration" - prevents artistic interpretations
        - Important for reproducibility and bias control
2. KSampler Parameters:
    - Steps (30):
        - Number of refinement iterations
        - Higher = more detail but diminishing returns
        - 30 balances quality with generation time
    - CFG (7.5): Classifier Free Guidance
        - Controls prompt adherence strength
        - 7.5 = balanced between creativity and prompt following
        - Lower values (1-5) = more creative/diverse
        - Higher values (8+) = more literal/strict
    - Sampler (euler/euler_ancestral):
        - Euler: More stable, consistent results
        - Euler_ancestral: Adds controlled randomness, potentially more natural
        - Choice affects reproducibility of results
    - Scheduler (normal):
        - Controls how quickly/slowly the image forms
        - "normal" provides standard pacing
    - Denoise (0.8):
        - Controls strength of the generation process
        - 0.8 allows some original image influence
        - 1.0 would be complete regeneration
3. Technical Settings:
    - Image Size (512x512):
        - Standard size for consistent quality
        - Balanced between detail and processing speed
        - Important for standardization across samples




- `base_workflow.json` is saved to `/Users/cindylinsf/Documents/CCI/THESIS/Msc_Thesis_Project_Files/models/ComfyUI/user/default/workflows`
    - This is the workflow with `euler` setting

### The first batch of testing generated very similar results

![Screenshot 2024-11-21 at 8.09.16 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7fa0be16-4a50-4137-a290-17d008668d2e/ac0383fc-f90d-4626-966b-bd8ca6a5120c/Screenshot_2024-11-21_at_8.09.16_PM.png)

1. Similar facial structure
2. Very similar eye shapes
3. Similar skin tone
4. Similar expressions

This could be due to several factors:

1. The base model (SDXL Turbo) might have its own biases in generating baby faces
2. The prompt we're using might be too specific/restrictive
3. The consistent parameters (CFG: 7.5, etc.) might be leading to similar outputs

### Randomize the parameters

1. Key Observations:
- The babies all have very similar facial features despite different donor inputs
- The lighting and pose are nearly identical
- The model seems to be overly influenced by the prompt rather than the donor images
1. Suggested Prompt-Parameter Adjustments:

Current issues:

- Base prompt might be too restrictive ("professional passport photo...")
- Similar lighting/background requirements creating uniformity
- Not enough donor features being incorporated

![Screenshot 2024-11-21 at 9.28.28 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7fa0be16-4a50-4137-a290-17d008668d2e/8462eed3-96d4-4208-be20-d07923a0f539/Screenshot_2024-11-21_at_9.28.28_PM.png)

![Screenshot 2024-11-21 at 9.26.59 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7fa0be16-4a50-4137-a290-17d008668d2e/b4893010-848f-4301-9310-bee2fb3a7d5e/Screenshot_2024-11-21_at_9.26.59_PM.png)

### **Modify two key elements**

**1. Modify the prompt in workflow for more variation:**

CURRENT:
"professional passport photo of a healthy 12 month old baby, front facing portrait, clean natural lighting, clear face, soft natural skin, white background, sharp focus, high quality photograph, Canon camera, photorealistic, no editing, neutral expression"

SUGGESTED NEW:
f"portrait of a 12 month old baby with distinctive facial features, natural pose, candid expression, detailed facial features, high quality photograph, photorealistic"

**2. Increase the influence of input images by adjusting these parameters:**

for node in modified['nodes']:
if node['type'] == 'KSampler':
parameters = {
'seed': random.randint(1, 2**31 - 1),
'steps': random.randint(35, 45),      # Increased
'cfg': round(random.uniform(4.0, 7.0), 1),  # Lowered for more image influence
'sampler': random.choice(['dpmpp_2m_sde', 'dpmpp_2m', 'euler_ancestral']),
'scheduler': 'karras',
'denoise': round(random.uniform(0.6, 0.75), 2)  # Lowered for more image influence
}

### batch test 4

![Screenshot 2024-11-22 at 10.59.02 AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7fa0be16-4a50-4137-a290-17d008668d2e/02a7ecf4-f401-4bdd-a952-e0a41465aacd/Screenshot_2024-11-22_at_10.59.02_AM.png)