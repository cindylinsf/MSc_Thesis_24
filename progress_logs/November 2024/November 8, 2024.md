# November 8, 2024

**Notes & Updates:** Visited University of Westminster Harrow Library to access Hito Steyerl’s books: ”I Will Survive”, “This is the Future”, “The City of Broken Windows”.
✅ Created data visualization of the current dataset
✅ Refining direction of the current thesis
✅ Read Steyerl’s essay In Defense of the Poor Image plus her books for the theoretical framework of the thesis

**Key Action:** Research on the theory framework side of the thesis; data visualization of the cleaned dataset

# Book: **Hito Steyerl: The city of broken windows Hardcover – 18 July 2019**

### Quotes from Essay by Carolyn Christov-Bakargiev

Page 36 “Data starts to drive the operation; it is not the programmers anymore but the data itself that defines what to do next. — E. Alpaydin, *Machine Learning: The New AI* (Cambridge, Mass. and London: The MIT Press, 2016)

[https://www.castellodirivoli.org/en/hito-steyerl-they-are-oblivious-to-the-violence-of-their-acts-windows-screens-and-pictorial-gestures-in-troubled-times/](https://www.castellodirivoli.org/en/hito-steyerl-they-are-oblivious-to-the-violence-of-their-acts-windows-screens-and-pictorial-gestures-in-troubled-times/)

---

# Thesis Direction Now

### 1. Data Augmentation:

- Create two sets:
    - Set A: Original distribution (control)
    - Set B: Balanced distribution (equal ethnic representation)

### 2. Process Flow:

- Original Profile → LLM Generation → Image Generation
- Augmented Profile → LLM Generation → Image Generation

### 3. Documentation Structure:

- Using one-by-one approach for clear documentation
- Track each profile transformation
- Maintain identical prompts across sets
- Document changes and biases

# Why Including Data Augmentation

### Example Scenario:

Original Data → Mostly Caucasian donors

↓

Generated Images → Strong bias toward Caucasian features

VS.

Augmented Data → More diverse donor profiles

↓

Generated Images → Still bias toward Caucasian features?

### Ideas to possibly show in the thesis:

- Side-by-side comparisons
- Visual evidence of persistent biases
- Where AI "fails" to imagine diversity

# What was done in the Data Augmentation

1. **Description Augmentation**:
    - Substitutes personality traits with meaningful synonyms
    - Varies physical descriptions while maintaining accuracy
    - Modifies hobby and interest descriptions with equivalent alternatives
    - Preserves the overall narrative structure
2. **Physical Trait Augmentation**:
    - Makes small, realistic variations in height (±1 inch)
    - Adjusts weight within realistic ranges (±5 lbs)
    - Maintains proper unit conversions (imperial to metric)
3. **Education Augmentation**:
    - Adds or modifies specializations within the same field
    - Maintains the education level while varying the specific focus areas

# Sophie Lewis’s book *Full Surrogacy Now*

Sophie Lewis's book "Full Surrogacy Now: Feminism Against Family" does touch on some aspects of modern fertility practices, particularly in relation to surrogacy. Here are the key points about Lewis's perspective on contemporary fertility practices:

## Ethical Concerns
- There are arguments that selling gametes could lead to a market for children or adults, potentially exploiting vulnerable populations (source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC479139/pdf/jmedeth00001-0026.pdf).

- Lewis suggests treating all motherhood as a consequence of capitalism, arguing that it should be appropriately remunerated (source: https://blogs.lse.ac.uk/gender/2023/07/12/who-can-afford-to-commodify-womens-bodies/).

- While some argue for treating gametes as commodities, there's a case for imposing restrictions to address moral, social, and economic concerns.
- The concept of "incomplete commodification" allows for the buying and selling of gametes with certain limitations.
 (source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC479139/pdf/jmedeth00001-0026.pdf)

## Global Inequalities
- Can also make an argument about **colonialsim in fertility** 
- The fertility industry often follows established routes of capital from South to North, poorer to more affluent bodies, and from Black and brown bodies to white ones.
- This pattern reinforces global hierarchies of gender, race, and class.
(source: https://blogs.lse.ac.uk/gender/2023/07/12/who-can-afford-to-commodify-womens-bodies/)

- Colonial Origins and Fertility: Can the Market Overcome History?: https://www.lshtm.ac.uk/newsevents/events/colonial-origins-and-fertility-can-market-overcome-history
    - https://kingcenter.stanford.edu/publications/working-paper/colonial-origins-and-fertility-can-market-overcome-history
    - https://www.theigc.org/sites/default/files/2021/07/BREAD2021_Canning_Mabeu_Pongou.pdf 
- Intertwined Colonial Pasts and the Present in Global Fertility Chains: https://catalystjournal.org/index.php/catalyst/article/view/37921/29157 


## Surrogacy as a Modern Fertility Practice

Lewis focuses extensively on gestational surrogacy, which she defines as "the practice of arranging a pregnancy in order to construct and deliver a baby that is 'someone else's'"[1]. She views surrogacy as a disruptive force that challenges traditional notions of family, parenthood, and reproduction. 

(source: https://blogs.lse.ac.uk/lsereviewofbooks/2020/08/07/book-review-full-surrogacy-now-feminism-against-family-by-sophie-lewis/)

## Critique of Commercial Surrogacy

While Lewis doesn't oppose surrogacy outright, she is critical of how it currently operates within neoliberal global marketplaces. She specifically examines practices at Dr. Patel's Akanksha Infertility Clinic as an example of contemporary commercial surrogacy.
(source: https://www.cambridge.org/core/journals/hypatia/article/full-surrogacy-now-feminism-against-family-sophie-lewis-london-verso-2019-isbn-9781786637291/712541C45D930B59741C102495FD4C49)

## Technology and Reproduction

Lewis draws influence from radical and cyborg feminists who embrace reproductive technologies like IVF and artificial wombs. She sees these technologies as potentially liberating forces that could transform social roles and family structures.

(source: https://www.cambridge.org/core/journals/hypatia/article/full-surrogacy-now-feminism-against-family-sophie-lewis-london-verso-2019-isbn-9781786637291/712541C45D930B59741C102495FD4C49)

## Commodification of Reproduction

The author discusses how modern fertility practices, particularly commercial surrogacy, intersect with capitalism. She argues that current practices often lead to the commodification of babies and reproduction.

(source: https://www.cambridge.org/core/journals/hypatia/article/full-surrogacy-now-feminism-against-family-sophie-lewis-london-verso-2019-isbn-9781786637291/712541C45D930B59741C102495FD4C49)

## Industry Trends

**Commercialization and Financialization**

- The fertility industry is experiencing increasing privatization and commercialization of fertility clinics.
- There's a trend towards financialization, with more money being generated through financial transactions rather than the production and trade of goods.

**Monopolization and Transnationalization**

- The industry is seeing tendencies towards monopolization through mergers and acquisitions.
- Transnationalization is evident, with corporations operating across state boundaries, often circumventing regulations and exploiting differences in laws and labor costs.

(source: https://sfb294-eigentum.de/en/blog/who-owns-and-controls-the-means-of-reproduction-assisted-fertility-and-pregnancy-as-a-multi-billion-dollar-market/)

## Reproductive Justice

Lewis incorporates perspectives on reproductive justice, acknowledging how access to and experiences with fertility practices are shaped by race and class. She references work by Black feminists who highlight historical and ongoing inequities in reproductive care.

(source: https://www.cambridge.org/core/journals/hypatia/article/full-surrogacy-now-feminism-against-family-sophie-lewis-london-verso-2019-isbn-9781786637291/712541C45D930B59741C102495FD4C49)

## Vision for Future Practices

Rather than simply critiquing current fertility practices, Lewis proposes a radical reimagining of reproduction and care. She advocates for a more communal approach to reproductive labor that goes beyond the traditional family structure.

While Lewis doesn't provide a comprehensive overview of all modern fertility practices, her work engages critically with surrogacy as a key aspect of contemporary reproduction, using it as a lens to examine broader issues of family, labor, and social organization.

(source: https://www.cambridge.org/core/journals/hypatia/article/full-surrogacy-now-feminism-against-family-sophie-lewis-london-verso-2019-isbn-9781786637291/712541C45D930B59741C102495FD4C49)
(source: https://blogs.lse.ac.uk/lsereviewofbooks/2020/08/07/book-review-full-surrogacy-now-feminism-against-family-by-sophie-lewis/)

Additional sources to look at: 
- https://www.societyandspace.org/articles/response-by-sophie-lewis-full-family-now-surrogacy-against-feminism
- https://onlinelibrary.wiley.com/doi/10.1111/padr.12363
- https://www.amazon.co.uk/Full-Surrogacy-Now-Sophie-Lewis/dp/1786637294
- https://www.versobooks.com/en-gb/products/711-full-surrogacy-now
- https://www.bostonreview.net/forum_response/sophie-lewis-lewis-emre/
- **https://www.gasworks.org.uk/2024/03/28/Gasworks_Reading_Group-Sophie_Lewis_Full_Surrogacy_Now.pdf**
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC479139/pdf/jmedeth00001-0026.pdf
- https://sfb294-eigentum.de/en/blog/who-owns-and-controls-the-means-of-reproduction-assisted-fertility-and-pregnancy-as-a-multi-billion-dollar-market/
- https://blogs.lse.ac.uk/gender/2023/07/12/who-can-afford-to-commodify-womens-bodies/
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4424057
- https://www.jstor.org/stable/26813127
- https://bioethics.pitt.edu/event/gametes-commodification-and-fertility-industry
- https://www.law.virginia.edu/scholarship/publication/kimberly-d-krawiec/1790116
- https://welltodo.substack.com/p/the-commodification-of-womens-health


## Hito Steyerl

Hito Steyerl's work and writing extensively cover digital image politics, technology critique, and platform capitalism:

## Digital Image Politics

Steyerl's art and writing frequently explore the politics of digital images and their circulation:

- In her essay "**Too Much World: Is the Internet Dead?**", Steyerl examines how digital images flow between virtual and physical spaces, shaping our perception of reality. (source: https://www.1854.photography/2021/07/the-real-and-the-virtual-hito-steyerl-navigates-the-increasing-indistinction-between-the-two-in-her-latest-exhibition/) She argues that the Internet has become a pervasive "mode of life" that influences everything from personal identities to political debates.
- Her video installation "**How Not to Be Seen: A Fucking Didactic Educational.MOV File**" (2013) critically examines the politics of visibility and invisibility in the digital age (source: https://www.1854.photography/2021/07/the-real-and-the-virtual-hito-steyerl-navigates-the-increasing-indistinction-between-the-two-in-her-latest-exhibition/).
- Steyerl's work often incorporates found images and video essays, using "the internet as a source of ready-made material" to confront political events and social issues (source: https://digmedia.lucdh.nl/2023/11/27/hito-steyerl-and-her-self-referential-works/).

## Technology Critique

Steyerl offers incisive critiques of modern technology and its societal impacts:

- Her installation "Hell Yeah We Fuck Die" (2016) combines video screens, robot sculptures, and techno music to critically examine robot technology and its testing (source: https://www.1854.photography/2021/07/the-real-and-the-virtual-hito-steyerl-navigates-the-increasing-indistinction-between-the-two-in-her-latest-exhibition/).
- "SocialSim" (2020) explores the potential and pitfalls of digitality, simulation, and artificial intelligence in the context of the COVID-19 pandemic (source: https://flash---art.com/article/hito-steyerl/).
- Steyerl's work often highlights how digital technologies shape surveillance, production, and social organization (source: https://www.1854.photography/2021/07/the-real-and-the-virtual-hito-steyerl-navigates-the-increasing-indistinction-between-the-two-in-her-latest-exhibition/).

## Platform Capitalism

Steyerl's art and writing frequently address the economic and power structures of digital platforms:

- She discusses how the Internet has become "monopolized and sanitized by common sense, copyright, control, and conformism". (source: https://www.1854.photography/2021/07/the-real-and-the-virtual-hito-steyerl-navigates-the-increasing-indistinction-between-the-two-in-her-latest-exhibition/)
- Her work examines how digital platforms owned by tech giants control the transmission of personal data. (source: https://www.1854.photography/2021/07/the-real-and-the-virtual-hito-steyerl-navigates-the-increasing-indistinction-between-the-two-in-her-latest-exhibition/)
- In recent comments, Steyerl critiques how companies like Microsoft are establishing "quasi-monopolies" over AI and cloud computing services, making users dependent on their infrastructure. (source: https://news.artnet.com/art-world/these-renderings-do-not-relate-to-reality-hito-steyerl-on-the-ideologies-embedded-in-a-i-image-generators-2264692)

Steyerl's approach is characterized by its self-referential nature, often using digital media to critique digital culture itself (source: https://digmedia.lucdh.nl/2023/11/27/hito-steyerl-and-her-self-referential-works/). 

Her exhibitions, like "I Will Survive," create immersive environments that confront viewers with the overwhelming nature of digital information and imagery[1][4]. Through her art and writing, Steyerl offers a complex, multifaceted critique of contemporary digital culture, capitalism, and technology. (source: https://digmedia.lucdh.nl/2023/11/27/hito-steyerl-and-her-self-referential-works/) (source: https://log.fakewhale.xyz/hito-steyerl-framing-the-global-imagery/)

Hito Steyerl's critique of digital image manipulation is a central theme in her work, addressing several key aspects:

## Subprime Visibility and Derivative Imagery

Steyerl introduces the concept of "derivative images" and "subprime visibility" to critique AI-generated imagery:

- She argues that AI-generated images are like financial derivatives, becoming wagers on visual culture rather than original creations.
- These images are composites, statistically averaged from vast datasets, often scraped without consent.
- The result is a "structural mediocrity" in images that lack depth and intentionality compared to traditional photography.

## Data Exploitation and Labor Issues

Steyerl highlights the exploitative nature of data extraction and labor in image generation:

- She compares data scraping to the extraction of raw materials in industrial economies.
- The artist draws attention to "ghost workers" - underpaid laborers who clean and annotate data for machine learning[1].
- This exploitation contributes to the "subprime" quality of AI-generated images.

## Collapse of Meaning

Steyerl warns about the potential loss of meaning in AI-generated imagery:

- She describes a "machine dementia" where image production is reduced to statistical probabilities.
- The recursive loop of AI generating content from its own output narrows the probability space, leading to repetitive, shallow visual content.
- This process threatens to erode trust in images as they increasingly reflect algorithmic biases rather than human vision or experience.

(source: https://aestheticsofphotography.com/subprime-images-by-hito-steyerl/)

## Poor Images and Circulation

Steyerl's work often focuses on the degradation of images through circulation:

- In her essay "In Defence of the Poor Image," she examines how digital images lose quality as they are shared and manipulated.
- She views this degradation as a form of visual abstraction that can have subversive qualities.
- Steyerl treats digital images as material objects, focusing on their physical properties and capacities rather than their immateriality.

(source: https://artreview.com/summer-2014-feature-hito-steyerl/)

## Manipulation and Reality Perception

The artist explores how image manipulation affects our perception of reality:

- Steyerl addresses how images can be distorted, decontextualized, and given new meanings.
- Her work challenges viewers to question the veracity and authenticity of the images they consume daily.
- She uses digital manipulation techniques to unveil complex narratives and critique the information society.

Steyerl's work serves as a profound inquiry into the nature of digital imagery in contemporary society, challenging conventions and inviting critical reflection on how we produce, consume, and interpret images in the digital age.

(source: https://log.fakewhale.xyz/hito-steyerl-framing-the-global-imagery/)


Additional sources to look at: 
- https://log.fakewhale.xyz/hito-steyerl-framing-the-global-imagery/
- https://flash---art.com/article/hito-steyerl/
- https://www.1854.photography/2021/07/the-real-and-the-virtual-hito-steyerl-navigates-the-increasing-indistinction-between-the-two-in-her-latest-exhibition/
- https://digmedia.lucdh.nl/2023/11/27/hito-steyerl-and-her-self-referential-works/
- https://news.artnet.com/art-world/these-renderings-do-not-relate-to-reality-hito-steyerl-on-the-ideologies-embedded-in-a-i-image-generators-2264692
- https://www.e-flux.com/criticism/238031/hito-steyerl-s-left-to-our-own-devices
- https://www.newyorker.com/culture/persons-of-interest/hito-steyerls-digital-visions
- https://aestheticsofphotography.com/subprime-images-by-hito-steyerl/
- https://artreview.com/summer-2014-feature-hito-steyerl/
- https://www.moma.org/collection/works/181784
- http://reusingoldgraves.weebly.com/articles/how-not-to-be-seen-hito-steyerls-civil-contract-of-representation
- https://thecomposingrooms.com/research/reading/2013/e-flux_Hito Steyerl_15.pdf


1. Reinforcement of Biases and Stereotypes:Steyerl's concept of "machine dementia" - where AI systems generate content based on narrow, repetitive datasets - could apply to AI-driven marketing. She might argue that such systems risk reinforcing existing biases and stereotypes, creating a feedback loop that narrows rather than expands cultural perspectives.
2. Erosion of Authenticity and Meaning:The artist has warned about the potential loss of meaning in AI-generated imagery. In marketing, this could translate to a critique of AI-generated content that lacks depth or genuine connection to human experiences, prioritizing engagement metrics over meaningful communication.
3. Commodification of Human Interaction:Steyerl might view AI in marketing as an extension of what she calls "platform capitalism." She could argue that it further commodifies human interactions and experiences, reducing complex social relationships to data points for algorithmic manipulation.
4. Subprime Visibility:Applying her concept of "subprime visibility," Steyerl might argue that AI-driven marketing creates a form of "subprime engagement" - interactions that appear valuable on the surface but lack substance or genuine human connection.

Hito Steyerl's critiques of AI and digital technologies can be highly relevant, especially regarding the **exploitation of emotional responses**. While Steyerl may not have directly addressed the fertility industry, her insights can be applied to this context. Here are some key points and potential references:

1. Emotional Vulnerability:
Steyerl's work often highlights how digital technologies can exploit human vulnerabilities. In the context of fertility marketing, AI could be used to target individuals at emotionally vulnerable moments, potentially exploiting their desires and anxieties around fertility.
2. Data Exploitation:
Steyerl has criticized the exploitative nature of data collection. In fertility marketing, this could relate to the use of personal health data, search histories, or social media activity to target individuals with fertility-related products or services.
3. Commodification of Human Experience:
Steyerl's critique of platform capitalism could be applied to how AI marketing in the fertility industry might commodify the deeply personal experience of trying to conceive.
4. Algorithmic Bias:
Steyerl's concerns about AI reproducing and amplifying societal biases could be relevant in discussing how AI marketing in fertility might reinforce certain stereotypes or exclude certain groups.

Some potential references:

1. Steyerl, H. (2017). Duty Free Art: Art in the Age of Planetary Civil War. Verso Books.
    - This book discusses how digital technologies shape our perception of reality, which could be applied to how AI marketing shapes perceptions of fertility.
2. Steyerl, H. (2009). In Defense of the Poor Image. e-flux Journal, 10.
    - While this essay focuses on image quality, its ideas about circulation and value in digital spaces could be applied to how fertility information and marketing spread online.
3. Steyerl, H. (2013). Too Much World: Is the Internet Dead? e-flux Journal, 49.
    - This essay discusses how the internet has become a pervasive "mode of life," which could be relevant to how AI marketing in fertility becomes part of individuals' daily digital experiences.
4. Crawford, K., & Joler, V. (2018). Anatomy of an AI System: The Amazon Echo As An Anatomical Map of Human Labor, Data and Planetary Resources. AI Now Institute and Share Lab.
    - While not by Steyerl, this work aligns with her critiques and provides a detailed analysis of the hidden costs of AI systems, which could be applied to fertility industry marketing.


- https://research.bangor.ac.uk/portal/files/71908170/Publishers-proof.pdf
- https://www.bruegel.org/blog-post/dark-side-artificial-intelligence-manipulation-human-behaviour
- https://www.forbes.com/sites/neilsahota/2024/07/29/the-dark-side-of-ai-is-how-bad-actors-manipulate-minds/
- https://hbr.org/2019/11/the-risks-of-using-ai-to-interpret-human-emotions
- https://trustcassie.com/resources/blog/emotion-ai-for-marketing/
- https://www.rathenau.nl/en/digitalisering/what-does-manipulative-ai-mean-consumers
- https://www.pbs.org/newshour/politics/ai-generated-disinformation-poses-threat-of-misleading-voters-in-2024-election
- https://www.technologyreview.com/2023/10/04/1080801/generative-ai-boosting-disinformation-and-propaganda-freedom-house/

Technical References:

1. Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K., & Galstyan, A. (2021). "A survey on bias and fairness in machine learning." ACM Computing Surveys (CSUR), 54(6), 1-35. [https://dl.acm.org/doi/10.1145/3457607](https://dl.acm.org/doi/10.1145/3457607)
    - This comprehensive survey provides an overview of bias in machine learning systems..
2. Buolamwini, J., & Gebru, T. (2018). "Gender shades: Intersectional accuracy disparities in commercial gender classification." Conference on fairness, accountability and transparency.
    1. [https://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf](https://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf)
    - This seminal work examines racial and gender biases in facial recognition systems, which could inform your analysis of generated donor images.

