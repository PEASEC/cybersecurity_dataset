# Cybersecurity Dataset
A dataset consisting of 4.3 million entries of Twitter, Blogs, Paper, and CVEs related to the cybersecurity domain 
---

| #Tokens | Min | Max | Sum | Median | Mean | Entries |
| --- | --- | --- | --- | --- | --- | --- |
| Blogs | 44 | 0.1M | 169M | 710 | 1.1k | 151k |
| arXiv | 533 | 0.7M | 167M | 8.2k | 9.9k | 16k |
| CVE | 5 | 1.9k | 12M | 58 | 71 | 171k |
| Twitter | 1 | 500 | 179M | 39 | 45 | 4M |
| Total | 1 | 0.7M | 528M | 40 | 122 | 4.3M |

**Table:** Statistics of the number of tokens and entries of the dataset.

**Blogs:** 38 different blogs, like troyhunt.com, darkreading.com, schneier.com, and krebsonsecurity.com | Filtered duplicates, non-english texts and instances shorter than 300 characters

**arXiv:** Papers from the category Cryptography and Security | Extraction: [opendetex](https://github.com/pkubowicz/opendetex) for papers in tex format and [textract](https://textract.readthedocs.io/en/stable/) for papers in pdf format | Filtered paper with lower length than 3000 characters

**CVEs:** NVD entries till 2022-03-15 21:38:23 | No filtering

**Twitter:** 1. Dataset: (infosec OR security OR threat OR vulnerability OR cyber OR cybersec OR infrasec OR netsec OR hacking OR siem OR soc OR offsec OR osing OR bugbounty) | 2. Dataset: Data breaches, as, for example, the Microsoft Exchange Server Data Breach

Usage
---
The dataset contains only the references to the data due to data storage/publication restrictions. The data instances can be gathered via the scripts in this repository or external tools.

Twitter Crawling: twitter_crawling.py -- Requirements: Installing [Tweepy](https://github.com/tweepy/tweepy)  For gathering the Tweets you need to insert your API-Key, API-Secret-Key, Access-Token and Access-Token-Secret of the Twitter-API into the script before you run it

Citation
---
When you use the dataset in your research, please cite: 

Bayer, M., Kuehn, P., Shanehsaz, R., & Reuter, C. (2022). CySecBERT: A Domain-Adapted Language Model for the Cybersecurity Domain. ArXiv, abs/2212.02974. 

https://arxiv.org/abs/2212.02974

Language Model
---
This is the dataset constitutes the training dataset of the [CySecBERT](https://huggingface.co/markusbayer/CySecBERT) model.
