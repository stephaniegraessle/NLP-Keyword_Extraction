# NLP-Keyword_Extraction

Tool for extracting keywords from a passage of text. WIP.

## Installation
Note: I found it easiest to run from a Linux terminal, such as [WSL (Windows Subsystem for Linux)](https://learn.microsoft.com/en-us/windows/wsl/install).

1. Download Python 3.
2. Install NLTK: `$ pip install nltk`
3. Run Python 3: `$ python3`
4. `>>> import nltk`
5. `>>> nltk.download('punkt')`
6. Exit from Python 3 with Ctrl-Z.
7. Install SpaCy Python module: `$ pip install spacy`
8. Download SpaCy English language package: `$ python3 -m spacy download en_core_web_sm`
9. Run program: `$ python3 main.py`

## Update log
2024-01-24
- Removes stopwords from text
