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

**Blogs:** 38 different blogs, like troyhunt.com, darkreading.com, schneier.com, and krebsonsecurity.com | Filtered duplicates, non-english texts and instances shorter than 300 characters)

**arXiv:** Papers from the category Cryptography and Security | Extraction: [opendetex](https://github.com/pkubowicz/opendetex) for papers in tex format and [textract](https://textract.readthedocs.io/en/stable/) for papers in pdf format | Filtered paper with lower length than 3000 characters

**CVEs:** NVD entries till 2022-03-15 21:38:23 | No filtering

**Twitter:** 1. Dataset: (infosec OR security OR threat OR vulnerability OR cyber OR cybersec OR infrasec OR netsec OR hacking OR siem OR soc OR offsec OR osing OR bugbounty) | 2. Dataset: Data breaches, as, for example, the Microsoft Exchange Server Data Breach

---
The dataset contains only the references to the data due to data storage/publication restrictions. All data instances can be crawled via tools like [Tweepy](https://github.com/tweepy/tweepy) or [Trafilatura](https://github.com/adbar/trafilatura).


