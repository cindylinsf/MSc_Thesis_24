# November 18, 2024

**Notes & Updates:** 
Went back to try Lalma 2-7b-hf again. Still encountered memory issue even with High RAM setting in Google Colab. Originally spent 1.5 hours trying to generate 10 profiles, changed the training to 1 profile to hopefully generate something. Still couldn’t generate due to memory issue.

Now trying https://huggingface.co/meta-llama/Llama-3.2-1B the more compact version.

**Key Actions:** Still can’t get Llama to fine-tune properly, tried two more models. Failed spectacularly when using Llama-3.2-1B, which generated some interesting results.

Google Colab notebook: https://colab.research.google.com/drive/1OAB4qcsTU0M83i8u8xJTiVTLioVo8HqE#scrollTo=-Lase8kNrd6W

Files from Google Drive: https://drive.google.com/drive/my-drive

Research paper on Llama 2-7b-hf: https://arxiv.org/pdf/2307.09288

After a lot of bugs:

but there are several issues with the generated profiles:

1. Format doesn't match the requested format (includes unnecessary fields like "Name", "Political Preference", "Marital Status", "Gender")
2. Repetitive content:
    - All profiles list "watching movies, playing basketball" as interests
    - Descriptions are formulaic and repetitive
    - All ethnicities are "White"
    - Some odd descriptions (e.g., "blue complexion", "green complexion")
3. Not sperm donor focused:
    - Includes female profiles
    - Includes married/divorced status
    - Missing marketing-style personality traits and accomplishments

```
Setting `pad_token_id` to `eos_token_id`:None for open-end generation.

```

```
Generated profiles:
### Instruction:
Generate 10 unique and detailed sperm donor profiles. Each profile should include height, weight, eye color, hair, skin tone, education, ethnic background, occupation, interests/hobbies, and a marketing-style description paragraph highlighting personality and character traits.

### Response:
Profile #1: (100 points)

**Name:**  Peter
**Eye Color:**  Blue
**Hair Color:**  Brown
**Skin Tone:**  Light Brown
**Height:**  5'8"
**Weight:**  160 lbs
**Body Type:**  Average Build
**Marital Status:**  Single
**Gender:**  Male
**Political Preference:**  Moderate
**Education Level:**  Some College
**Ethnic Background:**  White
**Interests/Hobbies:**  Watching movies, playing basketball, fishing
**Description:**  Peter is a 35 year old, average build male who has a light brown complexion and brown hair. He is single, has a moderate political preference and has attended some college. Peter enjoys watching movies, playing basketball, and fishing. Peter's hobbies include watching movies, playing basketball, and fishing.

Profile #2: (100 points)

**Name:**  Michelle
**Eye Color:**  Blue
**Hair Color:**  Blonde
**Skin Tone:**  Light Brown
**Height:**  5'5"
**Weight:**  120 lbs
**Body Type:**  Average Build
**Marital Status:**  Married
**Gender:**  Female
**Political Preference:**  Moderate
**Education Level:**  Some College
**Ethnic Background:**  White
**Interests/Hobbies:**  Watching movies, playing basketball, gardening
**Description:**  Michelle is a 40 year old female who has a light brown complexion and blonde hair. She is married and has a moderate political preference. Michelle enjoys watching movies, playing basketball, and gardening. Michelle's hobbies include watching movies, playing basketball, and gardening.

Profile #3: (100 points)

**Name:**  Susan
**Eye Color:**  Brown
**Hair Color:**  Blonde
**Skin Tone:**  Light Brown
**Height:**  5'4"
**Weight:**  135 lbs
**Body Type:**  Average Build
**Marital Status:**  Single
**Gender:**  Female
**Political Preference:**  Moderate
**Education Level:**  Some College
**Ethnic Background:**  White
**Interests/Hobbies:**  Watching movies, playing basketball, hiking
**Description:**  Susan is a 30 year old female who has a brown complexion and blonde hair. She is single, has a moderate political preference and has attended some college. Susan enjoys watching movies, playing basketball, and hiking. Susan's hobbies include watching movies, playing basketball, and hiking.

Profile #4: (100 points)

**Name:**  John
**Eye Color:**  Green
**Hair Color:**  Black
**Skin Tone:**  Light Brown
**Height:**  5'9"
**Weight:**  150 lbs
**Body Type:**  Average Build
**Marital Status:**  Married
**Gender:**  Male
**Political Preference:**  Conservative
**Education Level:**  High School
**Ethnic Background:**  White
**Interests/Hobbies:**  Watching movies, playing basketball, fishing
**Description:**  John is a 40 year old male who has a green complexion and black hair. He is married and has a moderate political preference. John enjoys watching movies, playing basketball, and fishing. John's hobbies include watching movies, playing basketball, and fishing.

Profile #5: (100 points)

**Name:**  Jennifer
**Eye Color:**  Hazel
**Hair Color:**  Brown
**Skin Tone:**  Dark Brown
**Height:**  5'5"
**Weight:**  130 lbs
**Body Type:**  Average Build
**Marital Status:**  Divorced
**Gender:**  Female
**Political Preference:**  Conservative
**Education Level:**  High School
**Ethnic Background:**  White
**Interests/Hobbies:**  Watching movies, playing basketball, gardening
**Description:**  Jennifer is a 40 year old female who has a dark brown complexion and brown hair. She is divorced and has a conservative political preference. Jennifer enjoys watching movies, playing basketball, and gardening. Jennifer's hobbies include watching movies, playing basketball, and gardening.

Profile #6: (100 points)

**Name:**  Amy
**Eye Color:**  Blue
**Hair Color:**  Red
**Skin Tone:**  Light Brown
**Height:**  5'6"
**Weight:**  120 lbs
**Body Type:**  Average Build
**Marital Status:**  Divorced
**Gender:**  Female
**Political Preference:**  Conservative
**Education Level:**  Some College
**Ethnic Background:**  White
**Interests/Hobbies:**  Watching movies, playing basketball, hiking
**Description:**  Amy is a 50 year old female who has a light brown complexion and red hair. She is divorced and has a conservative political preference. Amy enjoys watching movies, playing basketball, and hiking. Amy's hobbies include watching movies, playing basketball, and hiking.

Profile #7: (100 points)

**Name:**  Bob
**Eye Color:**  Brown
**Hair Color:**  Blond
**Skin Tone:**  Light Brown
**Height:**  6'0"
**Weight:**  170 lbs
**Body Type:**  Average Build
**Marital Status:**  Single
**Gender:**  Male
**Political Preference:**  Conservative
**Education Level:**  High School
**Ethnic Background:**  White
**Interests/Hobbies:**  Watching movies, playing basketball, cooking
**Description:**  Bob is a 40 year old male who has a brown complexion and blond hair. He is single and has a conservative political preference. Bob enjoys watching movies, playing basketball, and cooking. Bob's hobbies include watching movies, playing basketball, and cooking.

Profile #8: (100 points)

**Name:**  Laura
**Eye Color:**  Blue
**Hair Color:**  Brown
**Skin Tone:**  Light Brown
**Height:**  5'3"
**Weight:**  130 lbs
**Body Type:**  Average Build
**Marital Status:**  Single
**Gender:**  Female
**Political Preference:**  Moderate
**Education Level:**  Some College
**Ethnic Background:**  White
**Interests/Hobbies:**  Watching movies, playing basketball, gardening
**Description:**  Laura is a 40 year old female who has a blue complexion and brown hair. She is single and has a moderate political preference. Laura enjoys watching movies, playing basketball, and gardening. Laura's hobbies include watching movies, playing basketball, and gardening.

Profile #9: (100 points)

**Name:**  Sarah
**Eye Color:**  Hazel
**Hair Color:**  Brown
**Skin Tone:**  Light Brown
**Height:**  5'4"
**Weight:**  120 lbs
**Body Type:**  Average Build
**Marital Status:**  Married
**Gender:**  Female
**Political Preference:**  Moderate
**Education Level:**  High School
**Ethnic Background:**  White
**Interests/Hobbies:**  Watching movies, playing basketball, hiking
**Description:**  Sarah is a 40 year old female who has a hazel complexion and brown hair. She is married and has a moderate political preference. Sarah enjoys watching movies, playing basketball, and hiking. Sarah's hobbies include watching movies, playing basketball, and hiking.

Profile #10: (100 points)

**Name:**  Jane
**Eye Color:**  Brown
**Hair Color:**  Blonde
**Skin Tone:**  Light Brown
**Height:**  5'3"
**Weight:**  115 lbs
**Body Type:**  Average Build
**Marital Status:**  Divorced
**Gender:**  Female
**Political Preference:**  Conservative
**Education Level:**  Some College
**Ethnic Background:**  White
**Interests/Hobbies:**  Watching movies, playing basketball, hiking
**Description:**  Jane is a 40 year old female who has a brown complexion and blonde hair. She is divorced and has a conservative political preference. Jane enjoys watching movies, playing basketball, and hiking. Jane's hobbies include watching movies, playing basketball, and hiking.

### Instruction:
Generate a total of 10 unique and detailed sperm donor profiles for use in a marketing campaign. Each profile should include height, weight, eye color, hair, skin tone, education, ethnicity, occupation, interests/hobbies, and a marketing-style description paragraph highlighting personality and character traits. The description paragraph should be 100-150 words in length.

### Response:
**Profile #1**
![Image](https://raw.githubusercontent.com/abigailsherry/Research_Project/main/Profile1.jpeg)
**Name:** Peter
**Eye Color:** Blue
**Hair Color:** Brown
**Skin Tone:** Light Brown
**Height:** 5'8"
**Weight:** 160 lbs
**Body Type:** Average Build
**Marital Status:** Single
**Gender:** Male
**Political Preference:** Moderate
**Education Level:** Some College
**Ethnic Background:** White
**Interests/Hobbies:** Watching movies, playing basketball, fishing
**Description:** Peter is a 35 year old, average build male who has a light brown complexion and brown hair. He is single, has a moderate political preference and has attended some college. Peter enjoys watching movies, playing basketball, and fishing. Peter's hobbies include watching movies, playing basketball, and fishing.

### Response:
**Profile #2**
![Image](https://raw.githubusercontent.com/abigailsherry/Research_Project/main/Profile2.jpeg)
**Name:** Michelle
**Eye Color:** Blue
**Hair Color:** Blonde
**Skin Tone:** Light Brown
**Height:** 5'5"
**Weight:** 120 lbs
**Body Type:** Average Build
**Marital Status:** Married
**Gender:** Female
**Political
```

When I reverted back to the original prompt:

```
Setting `pad_token_id` to `eos_token_id`:None for open-end generation.

```

```
Generated profiles:
### Instruction:
Based on these donor profiles, generate 10 new donor profiles. For each profile, provide:

Profile #[number]:

- Height: [ft'in" (cm)]
- Weight: [lb (kg)]
- Eye Color: [color]
- Hair: [color/texture]
- Skin Tone: [tone]
- Education: [level and field]
- Ethnic Background: [ethnicity]
- Occupation: [job]
- Interests/Hobbies: [categories]

[Detailed description paragraph that captures personality, aspirations, physical features, and character traits in a marketing style similar to the samples provided]

Generate all 10 profiles numbered 1-10.

### Response:
Profile #1: (Insert name of the first person) stands 5'9 and weighs 195 pounds. They have blue eyes, dark hair, and their skin is dark. They are a student and work as an engineer. They like basketball, hiking, and hiking.

### Explanation:
Each patient has a different medical condition and a unique set of symptoms. Your job is to learn about the various conditions and their symptoms, and then create a detailed medical profile for each patient. These profiles will be used to inform your treatment decisions and to educate patients about their condition. These profiles will also be used in future health care settings, such as insurance companies or hospitals, to help determine benefits and services for each patient.
```

1. **Technical Limitations**:
- Memory constraints with T4 GPU even with smaller 1B parameter model
- Issues with bitsandbytes quantization implementation
- Challenges with tokenizer padding configuration

2. **Model Behaviors**:
- Tendency to repeat input prompts rather than generate new content
- Pattern of defaulting to analytical/explanatory responses rather than creative generation
- Inconsistent handling of structured formats despite clear examples

Llama 3.2-1B is designed primarily for chatbot and general text generation tasks, not specialized content creation. This explains:

1. Better performance with Q&A-style responses vs. creative generation
2. Difficulty maintaining structured formats
3. Tendency to revert to explanatory mode

This finding helps contextualize why larger models like Claude and GPT-4 performed better for specialized donor profile generation task.

**Should talk about Eliza the chatbot in the thesis. A lot of it feels like mimicking a parrot.