# November 15, 2024

**Notes & Updates:** 
Meeting 3 with Polo: 
- Include technical background of each model, introduce a blurb about it. Don’t assume the readers know every technical details in the paper (look at scientific papers for reference)
- Discussing artistic output in the thesis to tie back to the artists and theories that I have already planned
- Comparing fine-tuned vs. non-fine-tuned LLM outputs and analyzing the differences in how they generate donor profiles
- Looking at Stephanie Dinkins’ work https://www.stephaniedinkins.com/projects.html
>> Also look at Joanna Zylinska’s work again http://www.joannazylinska.net/publications/ and Trevor Paglen’s writing https://paglen.studio/

## Researching Llama models and editing documentation for the hand-in

While I downloaded Llama 3 versions, I ended up deciding to work with Llama 2 models instead. Llama 3 is still fairly new, versus Llama 2 has been extensively tested and documented by the community. There are also more established best practices for fine-tuning and more stable tooling and support.

- Using Llama out of the box https://www.meta.ai/
- Model documentation:
    - Getting started with Llama: https://www.llama.com/docs/overview/
    - Llama model cards on Github: https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md
- Models downloaded:
    - Llama 3.2: 1B & 3B
    - [https://llama3-2-lightweight.llamameta.net/*?Policy=eyJTdGF0ZW1lbnQiOlt7InVuaXF1ZV9oYXNoIjoieHAxM3ZhY3U5cTVqazlrMWcwM3VsN2V4IiwiUmVzb3VyY2UiOiJodHRwczpcL1wvbGxhbWEzLTItbGlnaHR3ZWlnaHQubGxhbWFtZXRhLm5ldFwvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTczMTg2MzEwMX19fV19&Signature=njaSageFUtgd8XhJ1CWOhiLHZT04GATlIYw~R1jILSQHPgf1AVei0~Oya7WTgqjiRds-87aGds~BMlTFQmyDVckN-k7RYuinI5lHtDTaLKHLUSJ7bH0Q~GGZ1ewzjL8qCnSRbUhPtiKhJwIhGC7upXUedqBY2trf73~RVrgQj1Hb7JI9dnPfiJc-NYl30KdcYgP-xVPoHQ3hp~KwFZd37Gjb8z10Dtf~t8P3LYMPm9uRtBUH2Be-XKasyQ1KAHYhi-xWnOtLC2xJiHXMrBW3XDoFNaAWtd01lNUOFEzXRCt~y4-GjNAknPjUgnZ0y2zzEMQdIUx9ZVglYaar~CzIHQ__&Key-Pair-Id=K15QRJLYKIFSLZ&Download-Request-ID=1645833412665242](https://llama3-2-lightweight.llamameta.net/*?Policy=eyJTdGF0ZW1lbnQiOlt7InVuaXF1ZV9oYXNoIjoieHAxM3ZhY3U5cTVqazlrMWcwM3VsN2V4IiwiUmVzb3VyY2UiOiJodHRwczpcL1wvbGxhbWEzLTItbGlnaHR3ZWlnaHQubGxhbWFtZXRhLm5ldFwvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTczMTg2MzEwMX19fV19&Signature=njaSageFUtgd8XhJ1CWOhiLHZT04GATlIYw%7ER1jILSQHPgf1AVei0%7EOya7WTgqjiRds-87aGds%7EBMlTFQmyDVckN-k7RYuinI5lHtDTaLKHLUSJ7bH0Q%7EGGZ1ewzjL8qCnSRbUhPtiKhJwIhGC7upXUedqBY2trf73%7ERVrgQj1Hb7JI9dnPfiJc-NYl30KdcYgP-xVPoHQ3hp%7EKwFZd37Gjb8z10Dtf%7Et8P3LYMPm9uRtBUH2Be-XKasyQ1KAHYhi-xWnOtLC2xJiHXMrBW3XDoFNaAWtd01lNUOFEzXRCt%7Ey4-GjNAknPjUgnZ0y2zzEMQdIUx9ZVglYaar%7ECzIHQ__&Key-Pair-Id=K15QRJLYKIFSLZ&Download-Request-ID=1645833412665242)
        - Marketed as “Lightweight”
        - Lightweight and most cost-efficient models you can run anywhere on mobile and on edge devices.
        - Llama Guard 3 1B is included.
        - Quantized models available
        - Licensed under Llama 3.2 Community License Agreement
    - Llama 3.2: 11B & 90B
        - Marketed as “Multimodal”
        - [https://llama3-2-multimodal.llamameta.net/*?Policy=eyJTdGF0ZW1lbnQiOlt7InVuaXF1ZV9oYXNoIjoiNGVsM2I2anJucWJwcnVmbHA5bnBxZzQ2IiwiUmVzb3VyY2UiOiJodHRwczpcL1wvbGxhbWEzLTItbXVsdGltb2RhbC5sbGFtYW1ldGEubmV0XC8qIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzMxODYzMTAxfX19XX0_&Signature=bLimDqafuUMRRIuxHZwbF3nJJRa87yCJZC8KrLjZxckVq8mL9ZOztqskj9KehP4x8YkI3AQW2ymEdKTY8la9IrmL-wyuS0t8KXpKQdqMUyrlWvxf5syU4A8MobdpHOEEipJEzgicA6UnoNzbDxZLfIBqw6P4VdVpl2EGj31wwY9YGyWwtymviZa4MPpU4QnykIJCO26EEI3RvUxLxhXegh1TGkCzM5K50cmhPt3tq4LwJV5COUx0vqsDzb5DVGaczVXums6v9am4lLdnTA7f9VS-vVSFff0yKoqlSmLAMchrbj1TDfqB~NkgTFB3RaiHVKydLSjBeXP443S1uzgJiA__&Key-Pair-Id=K15QRJLYKIFSLZ&Download-Request-ID=3844362312498525](https://llama3-2-multimodal.llamameta.net/*?Policy=eyJTdGF0ZW1lbnQiOlt7InVuaXF1ZV9oYXNoIjoiNGVsM2I2anJucWJwcnVmbHA5bnBxZzQ2IiwiUmVzb3VyY2UiOiJodHRwczpcL1wvbGxhbWEzLTItbXVsdGltb2RhbC5sbGFtYW1ldGEubmV0XC8qIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzMxODYzMTAxfX19XX0_&Signature=bLimDqafuUMRRIuxHZwbF3nJJRa87yCJZC8KrLjZxckVq8mL9ZOztqskj9KehP4x8YkI3AQW2ymEdKTY8la9IrmL-wyuS0t8KXpKQdqMUyrlWvxf5syU4A8MobdpHOEEipJEzgicA6UnoNzbDxZLfIBqw6P4VdVpl2EGj31wwY9YGyWwtymviZa4MPpU4QnykIJCO26EEI3RvUxLxhXegh1TGkCzM5K50cmhPt3tq4LwJV5COUx0vqsDzb5DVGaczVXums6v9am4lLdnTA7f9VS-vVSFff0yKoqlSmLAMchrbj1TDfqB%7ENkgTFB3RaiHVKydLSjBeXP443S1uzgJiA__&Key-Pair-Id=K15QRJLYKIFSLZ&Download-Request-ID=3844362312498525)
        - Open multimodal models that are flexible and can reason on high resolution images and output text.
        - Llama Guard 3 11B Vision is included
        - Licensed under Llama 3.2 Community License Agreement
    - Llama 3.1: 405B, 70B & 8B
        - Marketed as “Text” model
        - [https://llama3-1.llamameta.net/*?Policy=eyJTdGF0ZW1lbnQiOlt7InVuaXF1ZV9oYXNoIjoiem4xMWZrbmlxdTljZXMzcHBpcGdndnpxIiwiUmVzb3VyY2UiOiJodHRwczpcL1wvbGxhbWEzLTEubGxhbWFtZXRhLm5ldFwvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTczMTg2MzEwMX19fV19&Signature=Q9mqGjVcFADV8gsAzYQgASJDzxkzmrO3-8KM7j9P3UAptsuR6TAeKzW2aIcPaPTa1FR~4E4K-Qa88TX66Mg~hTfARZwg4xLfa0JUh~iotbn0lglzBuZ5FDCjagsSFls9gjrHTw1X3i02pV-jr9P5wZWW8G951P9bHrz4zq1HR1dYnOrGnEU8Tu0JjtkGV2~eJ3LLdxnKFCNPo0mdwzIzcDuQ~TTGRI72AfWYag~6xri1DYJH2ORh1jv0QIFSsq3BgoWM2xU6BrS1~eGBRvxiCZMmhE53UVEDfwjqOLRooLH7ZyT5rEqAaOQiLfB3cflxcgAKBsCBUTWOT05HHRrULw__&Key-Pair-Id=K15QRJLYKIFSLZ&Download-Request-ID=550719167824440](https://llama3-1.llamameta.net/*?Policy=eyJTdGF0ZW1lbnQiOlt7InVuaXF1ZV9oYXNoIjoiem4xMWZrbmlxdTljZXMzcHBpcGdndnpxIiwiUmVzb3VyY2UiOiJodHRwczpcL1wvbGxhbWEzLTEubGxhbWFtZXRhLm5ldFwvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTczMTg2MzEwMX19fV19&Signature=Q9mqGjVcFADV8gsAzYQgASJDzxkzmrO3-8KM7j9P3UAptsuR6TAeKzW2aIcPaPTa1FR%7E4E4K-Qa88TX66Mg%7EhTfARZwg4xLfa0JUh%7Eiotbn0lglzBuZ5FDCjagsSFls9gjrHTw1X3i02pV-jr9P5wZWW8G951P9bHrz4zq1HR1dYnOrGnEU8Tu0JjtkGV2%7EeJ3LLdxnKFCNPo0mdwzIzcDuQ%7ETTGRI72AfWYag%7E6xri1DYJH2ORh1jv0QIFSsq3BgoWM2xU6BrS1%7EeGBRvxiCZMmhE53UVEDfwjqOLRooLH7ZyT5rEqAaOQiLfB3cflxcgAKBsCBUTWOT05HHRrULw__&Key-Pair-Id=K15QRJLYKIFSLZ&Download-Request-ID=550719167824440)
        - State-of-the-art multilingual open source large language model
        - Llama Guard 3 8B and Prompt Guard are included
        - Licensed under Llama 3.1 Community License Agreement
- Meta’s documentation on how to **fine-tune**: https://www.llama.com/docs/how-to-guides/fine-tuning
    - https://github.com/meta-llama/llama-recipes/blob/main/docs/LLM_finetuning.md