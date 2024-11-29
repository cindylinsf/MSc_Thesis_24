# November 7, 2024

**Notes & Updates:** 

bank1: 435 profiles
bank2: 126 profiles
bank3: 68 profiles
bank4: 390 profiles
Total: 1019 profiles
About 12% of the profiles are EU-based donors vs. 88% of donors are US-based

**Key Action:** Dataset cleaning

### Data Cleaning Summary

1. **donor_description**
    - Merged narrative elements: primary descriptions, staff impressions, personal goals
    - Excluded: astrological signs, favorite pets
        - They only existed in one database
    - Format: Organized with labeled sections for clarity and context
2. **Physical Attributes**
    - height
    - weight
    - eye_color
    - hair_color
    - skin_tone
    - Rationale: These are consistent, objective characteristics present across most datasets
3. **Background Information**
    - education_level & education_field
        - Merged: areas of study into education_field
        - Purpose: Separate fields allow for more structured analysis
    - ethnic_background
        - Merged: nationality, jewish ancestry, mother's/father's ethnicity, race
        - Rationale: Consolidates all heritage-related information while preserving context
    - religion
        - Maintained as separate field for context
    - occupation
        - Maintained as separate field for context
    - interests_hobbies
        - Merged: skills, talents, interests
        - Purpose: Personal characteristics and activities can be good background/context information for the LLM to generate more details.

**Key Decisions:**

1. **Privacy**
    - Removed: IDs and source bank information
    - Prevent potential tracking or identification
2. **Data Consolidation**
    - Merged similar fields to create consistent structure
    - Maintained separation where distinct information types exist
    - Focus on preserving context while reducing redundancy
3. **Discarded Elements:**
    - Astrological signs
    - Favorite pets
    - Other one-off personal trivia
    Rationale:
    - Only one data source included these additional elements, so I was afraid that it would become noise for LLM and becomes distracting
    - Maintain focus on core characteristics that essentially every bank includes

### Data Cleaning Considerations

During data cleaning, I made the decision to preserve original spellings in the descriptions. Here are the following reasoning:

- Modern LLMs are trained on diverse English variants, where LLMs can understand semantic equivalence across spelling differences, even misspelled words
- It could be interesting to see if LLMs generate any English variants in its generation
- Retaining cultural and geographic context
- Since some of the donor descriptions include quotes from donors and staff impressions, by retaining the wording retains the original voice and background of the donors

## Research on cultural bias in NLP systems

- Search results
    
    Based on the search results provided, there has been significant research on cultural bias in NLP systems. Here are some key findings and insights:
    
    1. Cultural bias in language models:
    - Large language models (LLMs) trained predominantly on English text exhibit a latent bias favoring Western cultural values, especially when prompted in English [2].
    - LLMs tend to produce outputs that align with cultural values of English-speaking and Protestant European countries by default [2].
    1. Sources of cultural bias:
    - NLP datasets composed of utterances from members of a larger culture reflect that culture's values, norms, and ethics [1].
    - The overrepresentation of certain parts of the world in training corpora leads to hidden cultural biases in how LLMs generate and interpret language [2].
    1. Types of cultural bias:
    - Gender bias: Pervasive problem with sexism in models, reflecting sexist attitudes present in society [1].
    - Ethnic and racial bias: Language models produce racially biased language and struggle with underrepresented dialects and accents [3].
    - Religious bias: Models can produce offensive or biased content related to various religions [3].
    1. Impact of cultural bias:
    - Can reinforce stereotypes and lead to discrimination based on gender, ethnicity, race, religion, and economic background [3].
    - May limit opportunities for certain groups, e.g., recommending careers based on gender stereotypes [3].
    1. Evaluation of cultural bias:
    - Researchers have developed benchmarks like BLEnD to evaluate LLMs' everyday knowledge across diverse cultures and languages [4].
    - Studies show significant performance gaps between well-represented cultures/languages and underrepresented ones [4].
    1. Mitigation strategies:
    - Cultural prompting: Specifying cultural identity in prompts can improve cultural alignment for most countries with recent models [2].
    - Diversifying training data and including underrepresented groups [3].
    - Fine-tuning models on culturally relevant data, though this requires significant resources [2].
    - Employing techniques like adversarial training to reduce biased language generation [3].
    1. Challenges in addressing cultural bias:
    - Balancing multicultural pluralism (respecting different cultural values) with societal equity (minimizing harmful cultural biases) [1].
    - Need for collaboration with members of relevant cultures to navigate complex cultural issues [1].
    1. Future directions:
    - Developing more comprehensive taxonomies of cultural elements to systematically analyze and address cultural bias in NLP [5].
    - Creating culturally aware and adapted NLP systems that can appropriately handle diverse cultural contexts [5].
    
    This research highlights the importance of addressing cultural bias in NLP systems to ensure fair and equitable language technology for users from diverse cultural backgrounds.
    
    Citations:
    [1] [https://aclanthology.org/2022.acl-long.482.pdf](https://aclanthology.org/2022.acl-long.482.pdf)
    [2] [https://academic.oup.com/pnasnexus/article/3/9/pgae346/7756548](https://academic.oup.com/pnasnexus/article/3/9/pgae346/7756548)
    [3] [https://www.johnsnowlabs.com/unmasking-the-biases-within-ai-how-gender-ethnicity-religion-and-economics-shape-nlp-and-beyond/](https://www.johnsnowlabs.com/unmasking-the-biases-within-ai-how-gender-ethnicity-religion-and-economics-shape-nlp-and-beyond/)
    [4] [https://arxiv.org/html/2406.09948v1](https://arxiv.org/html/2406.09948v1)
    [5] [https://arxiv.org/html/2406.03930v1](https://arxiv.org/html/2406.03930v1)
    [6] [https://ec.europa.eu/futurium/en/system/files/ged/shared_racial_bias_in_natural_language_processing_-_report.pdf](https://ec.europa.eu/futurium/en/system/files/ged/shared_racial_bias_in_natural_language_processing_-_report.pdf)
    [7] [https://www.brookings.edu/articles/detecting-and-mitigating-bias-in-natural-language-processing/](https://www.brookings.edu/articles/detecting-and-mitigating-bias-in-natural-language-processing/)
    [8] [https://www.pure.ed.ac.uk/ws/portalfiles/portal/352548259/Biases_in_Large_NAVIGLI_DOA02022023_AFV_CC_BY.pdf](https://www.pure.ed.ac.uk/ws/portalfiles/portal/352548259/Biases_in_Large_NAVIGLI_DOA02022023_AFV_CC_BY.pdf)
    

### Work on de-colonial approaches to NLP

**This could be an interesting discussion point in the paper**

- Search Results
    
    Based on the search results provided, there are several key themes and approaches related to decolonial work in NLP:
    
    1. Addressing power dynamics and data colonialism:
    - The paper "Decolonizing African NLP" explores how colonial legacies impact NLP research and development, leading to marginalization of African languages, cultures and voices [1].
    - It advocates for diversifying representation, empowering local communities, and challenging Eurocentric frameworks in NLP [1].
    1. Promoting linguistic equity and diversity:
    - There's recognition of an imbalance in NLP training data, with English being vastly overrepresented (e.g. 92.65% of GPT-3 training tokens) [5].
    - This leads to performance disparities across languages, with models performing better on high-resource languages like English compared to low-resource languages [5].
    1. Centering African languages and perspectives:
    - Projects like Masakhane aim to advance NLP research specifically for African languages, challenging the status quo of prioritizing widely spoken languages [1].
    - The MasakhaNER project is described as being "by Africans, for Africans" to bring more African languages into NLP [4].
    1. Promoting data sovereignty and ethical practices:
    - There's emphasis on the need for data sovereignty, community ownership of data, and ethical data practices in African NLP [1].
    - Relational ethics approaches are suggested to link personhood to communities and foreground historical injustices [4].
    1. Developing culturally-aware NLP:
    - Recent work has proposed taxonomies of cultural elements to systematically analyze and develop culturally-aware NLP systems [5].
    - This includes considering linguistic forms, values, common ground, and social interactions across cultures [5].
    1. Critical approaches to AI development:
    - Decolonial theories are proposed as a form of sociotechnical foresight for AI development [3].
    - This involves creating critical technical practices, seeking reverse tutelage, and renewing affective/political communities [3].
    1. Interdisciplinary collaboration:
    - There are calls for interdisciplinary collaboration between NLP researchers, social scientists, and communities to advance decolonial approaches [1][3].
    
    In summary, decolonial approaches to NLP focus on addressing historical power imbalances, promoting linguistic and cultural diversity, centering marginalized perspectives, ensuring ethical data practices, and developing more inclusive and equitable AI technologies. This often involves critical examination of existing practices and close collaboration with affected communities.
    
    Citations:
    [1] [https://openreview.net/pdf?id=D698BEfwgv](https://openreview.net/pdf?id=D698BEfwgv)
    [2] [https://openreview.net/forum?id=D698BEfwgv](https://openreview.net/forum?id=D698BEfwgv)
    [3] [https://link.springer.com/article/10.1007/s13347-020-00405-8](https://link.springer.com/article/10.1007/s13347-020-00405-8)
    [4] [https://ojs.stanford.edu/ojs/index.php/grace/article/download/2584/1546/9011](https://ojs.stanford.edu/ojs/index.php/grace/article/download/2584/1546/9011)
    [5] [https://arxiv.org/html/2406.03930v1](https://arxiv.org/html/2406.03930v1)
    [6] [https://www.tandfonline.com/doi/full/10.1080/1369118X.2021.1986102](https://www.tandfonline.com/doi/full/10.1080/1369118X.2021.1986102)
    [7] [https://www.demography.ox.ac.uk/news/decolonising-computational-sociology](https://www.demography.ox.ac.uk/news/decolonising-computational-sociology)
    [8] [https://dl.acm.org/doi/fullHtml/10.1145/3465416.3483301](https://dl.acm.org/doi/fullHtml/10.1145/3465416.3483301)
    

### "Cross-cultural robustness of LLMs"

- Search Results
    
    Based on the search results provided, there are several key insights regarding the cross-cultural robustness of large language models (LLMs):
    
    1. Performance disparities across languages and cultures:
    - LLMs generally perform better on high-resource languages like English, German, and French compared to low-resource languages [5].
    - There are significant performance gaps between well-represented cultures/languages and underrepresented ones [2].
    - For example, GPT-4 showed a maximum 57.34% difference in performance between highly represented and underrepresented cultures on a benchmark of everyday cultural knowledge [2].
    1. Cultural alignment challenges:
    - LLMs often exhibit unbalanced cultural knowledge and unfair cultural biases across various countries and regions [2].
    - Studies using Hofstede's cultural dimensions framework found weak correlations between LLM outputs and expected cultural values for different countries, indicating cultural misalignment [3][4].
    - GPT-4 demonstrated stronger understanding of cultural dimensions compared to other LLMs, but still faced challenges aligning with non-US cultures [3][4].
    1. Language-specific performance:
    - For cultures represented by mid-to-high-resource languages, LLMs tend to perform better in local languages [2].
    - However, for cultures represented by low-resource languages, LLMs often perform better in English than the local languages [2].
    1. Improving cross-cultural capabilities:
    - Some researchers are exploring methods like cross-lingual instruction tuning to improve LLMs' performance on non-English languages [1].
    - Specifying a persona's nationality in prompts was found to improve cultural alignment to some degree [4].
    1. Evaluation methods:
    - New benchmarks like BLEnD have been developed to evaluate LLMs' everyday cultural knowledge across diverse cultures and languages [2].
    - Researchers have proposed methods like the Cultural Alignment Test (CAT) based on Hofstede's dimensions to assess LLMs' cultural alignment [3][4].
    1. Ongoing challenges:
    - There's a need for more diverse and representative training data, especially for underrepresented languages and cultures [2][5].
    - Addressing cultural biases and improving cross-cultural robustness remains an important area for future research and development of LLMs [2][3][4].
    
    In summary, while LLMs have made progress in cross-cultural capabilities, there are still significant challenges in achieving robust performance across diverse languages and cultures, particularly for underrepresented groups. Ongoing research focuses on developing better evaluation methods, improving training data diversity, and exploring techniques to enhance cross-cultural understanding in LLMs.
    
    Citations:
    [1] [https://openreview.net/forum?id=CaP3CByuLp](https://openreview.net/forum?id=CaP3CByuLp)
    [2] [https://arxiv.org/html/2406.09948v1](https://arxiv.org/html/2406.09948v1)
    [3] [https://globalaicultures.github.io/pdf/14_cultural_alignment_in_large_la.pdf](https://globalaicultures.github.io/pdf/14_cultural_alignment_in_large_la.pdf)
    [4] [https://montrealethics.ai/how-culturally-aligned-are-large-language-models/](https://montrealethics.ai/how-culturally-aligned-are-large-language-models/)
    [5] [https://arxiv.org/html/2404.11553v1](https://arxiv.org/html/2404.11553v1)
    [6] [https://arxiv.org/html/2405.15145v1](https://arxiv.org/html/2405.15145v1)
    [7] [https://aclanthology.org/2023.c3nlp-1.12.pdf](https://aclanthology.org/2023.c3nlp-1.12.pdf)
    [8] [https://www.degruyter.com/document/doi/10.1515/jtc-2023-0019/html?lang=en](https://www.degruyter.com/document/doi/10.1515/jtc-2023-0019/html?lang=en)
    

### "Language model bias and regional English"

- Search Results
    
    Based on the search results provided, there are several key insights regarding language model bias and regional English variants:
    
    1. Regional bias within English:
    - Research has found evidence of regional bias even within monolingual English language models, affecting performance across different English-speaking regions [1][2].
    - Subtle geographic variations in word embeddings were observed in BERT, even between cultures traditionally perceived as similar [1][2].
    1. Performance disparities:
    - Models generally exhibit better performance on datasets that share similarities with their training data [1][2].
    - Performance may diverge when datasets contain nuanced features or regional variations not well-represented in the training data [1][2].
    1. Bias towards "standard" varieties:
    - ChatGPT was found to default to "standard" varieties of English (American and British) when responding to prompts [3].
    - Responses to non-"standard" varieties exhibited issues like lack of comprehension, stereotyping, demeaning content, and condescending responses [3].
    1. Cultural bias:
    - Large language models trained predominantly on English text exhibit latent bias favoring Western cultural values [4].
    - Models like GPT-3 and GPT-4 were found to produce outputs aligning with cultural values of English-speaking and Protestant European countries by default [4].
    1. Performance across languages and cultures:
    - There are significant performance gaps between well-represented cultures/languages and underrepresented ones [5].
    - For cultures represented by mid-to-high-resource languages, LLMs tend to perform better in local languages [5].
    - For cultures represented by low-resource languages, LLMs often perform better in English than the local languages [5].
    1. Mitigation strategies:
    - Cultural prompting (specifying cultural identity in prompts) has shown some success in improving cultural alignment for recent models [4].
    - However, challenges remain in balancing multicultural representation while minimizing harmful biases.
    
    These findings highlight the need for more diverse and representative training data, especially for underrepresented languages and regional English variants. They also underscore the importance of developing evaluation methods that can capture nuanced linguistic and cultural differences to ensure fair and accurate performance across different English-speaking regions and cultures.
    
    Citations:
    [1] [https://www.ethicalcomputing.auckland.ac.nz/research-project-regional-bias-in-monolingual-english-language-models/](https://www.ethicalcomputing.auckland.ac.nz/research-project-regional-bias-in-monolingual-english-language-models/)
    [2] [https://wickerlab.org/publication/regional-bias-in-monolingual-english-language-models/](https://wickerlab.org/publication/regional-bias-in-monolingual-english-language-models/)
    [3] [https://arxiv.org/html/2406.08818v1](https://arxiv.org/html/2406.08818v1)
    [4] [https://academic.oup.com/pnasnexus/article/3/9/pgae346/7756548](https://academic.oup.com/pnasnexus/article/3/9/pgae346/7756548)
    [5] [https://arxiv.org/html/2406.09948v1](https://arxiv.org/html/2406.09948v1)
    [6] [https://ojs.stanford.edu/ojs/index.php/grace/article/download/2584/1546/9011](https://ojs.stanford.edu/ojs/index.php/grace/article/download/2584/1546/9011)
    [7] [https://www.nature.com/articles/d41586-024-02839-y](https://www.nature.com/articles/d41586-024-02839-y)
    [8] [https://globalaicultures.github.io/pdf/14_cultural_alignment_in_large_la.pdf](https://globalaicultures.github.io/pdf/14_cultural_alignment_in_large_la.pdf)
    

### THIS!

*Find research papers that discuss methodological decisions in preparing textual data for LLM analysis, specifically regarding preservation of language variants and spelling differences. Include studies that justify maintaining original linguistic features in datasets.*

- Search Results
    
    Based on the search results and recent research, there are limited studies specifically addressing methodological decisions around preserving language variants and spelling differences when preparing textual data for large language model (LLM) analysis. However, I can provide some relevant insights from related research:
    
    ## Importance of Linguistic Diversity
    
    A 2023 paper in Ethics and Information Technology introduced the concept of "language modeling bias", highlighting how language technology often favors certain languages or dialects over others[1]. This suggests that preserving linguistic diversity in training data is crucial.
    
    Key points:
    
    - Language modeling bias can result in systems that are precise for dominant languages/cultures but limited in expressing concepts from other communities.
    - Developing language technology primarily from the perspective of a single language (often English) can lead to epistemic injustice by inadequately representing linguistic diversity.
    
    ## Spelling Convention Sensitivity
    
    A 2023 study published in the Findings of EACL examined whether large neural language models learn dependencies based on orthographic cues to language variety, focusing on British vs American English spelling conventions[1].
    
    Findings relevant to data preparation:
    
    - Language models trained on web-scraped English data encounter multiple English varieties, including British English, North American English, and various World Englishes.
    - The researchers found evidence of a "heavy overall skew towards US spelling variants" in typical training data, leading to higher prior probabilities for American spellings in the models.
    
    This suggests that maintaining original spelling variants in datasets could be important for preserving linguistic diversity and reducing bias towards dominant variants.
    
    ## Character-Level Understanding
    
    A 2024 paper on arXiv examined large language models' ability to understand the character composition of words[1]. While not directly addressing data preparation, the findings have implications for preserving spelling differences:
    
    - Most contemporary LLMs struggle with reliably understanding the character composition of words.
    - Even basic character-level tasks proved challenging for many LLMs.
    
    This indicates that preserving original spellings and linguistic features in training data could be crucial for improving LLMs' ability to process fine-grained language differences.
    
    ## Justifications for Maintaining Original Linguistic Features
    
    While there's a lack of studies explicitly justifying the preservation of original linguistic features in LLM datasets, we can infer some reasons based on the research:
    
    1. Linguistic diversity: Maintaining original spellings and variants helps preserve the richness of language diversity in the data.
    2. Reduced bias: Keeping diverse linguistic features can help counteract the tendency of models to favor dominant language variants (e.g., American English spellings).
    3. Improved character-level understanding: Exposing models to diverse spellings and linguistic features may help improve their ability to process fine-grained language differences.
    4. Cultural representation: Preserving original linguistic features ensures better representation of different cultures and language communities in the model's training data.
    5. Enhanced model robustness: Exposure to diverse linguistic features during training may improve the model's ability to handle variations in real-world language use.
    
    While these justifications are not explicitly stated in the available research, they align with the broader goals of reducing bias and improving linguistic diversity in language models. Further research specifically addressing methodological decisions in data preparation for LLMs, particularly regarding language variants and spelling differences, would be valuable to provide more concrete guidance in this area.
    
    Citations:
    [1] [https://arxiv.org/html/2402.17385v1](https://arxiv.org/html/2402.17385v1)
    [2] [https://assets.amazon.science/cb/be/61fb549d46aea9850d7ed11edf73/reconciling-methodological-paradigms-employing-large-language-models-as-novice-qualitative-research-assistants-in-talent-management-research.pdf](https://assets.amazon.science/cb/be/61fb549d46aea9850d7ed11edf73/reconciling-methodological-paradigms-employing-large-language-models-as-novice-qualitative-research-assistants-in-talent-management-research.pdf)
    [3] [https://unece.org/sites/default/files/2024-03/LLM for Methodological advise_0.pdf](https://unece.org/sites/default/files/2024-03/LLM%20for%20Methodological%20advise_0.pdf)
    [4] [https://www.qualitative-research.net/index.php/fqs/article/view/4196](https://www.qualitative-research.net/index.php/fqs/article/view/4196)
    [5] [https://systematicreviewsjournal.biomedcentral.com/articles/10.1186/s13643-024-02609-x](https://systematicreviewsjournal.biomedcentral.com/articles/10.1186/s13643-024-02609-x)
    [6] [https://en.wikipedia.org/wiki/Large_language_model](https://en.wikipedia.org/wiki/Large_language_model)
    [7] [https://arxiv.org/html/2312.07819v1](https://arxiv.org/html/2312.07819v1)
    [8] [https://aclanthology.org/2022.bigscience-1.3.pdf](https://aclanthology.org/2022.bigscience-1.3.pdf)