# News Article Text Analyzer

A Python-based text analysis tool that processes an input text file (`article.txt`) to generate structural and lexical metrics, including paragraph, sentence, and word counts.

## Features
* **Sentence Counting:** Counts total sentences using key punctuation marks (`.`, `!`, `?`).
* **Paragraph Counting:** Detects distinct structural paragraphs separated by double line breaks (`\n\n`).
* **Word Analysis:** Tracks frequency metrics to identify the most frequent word and counts specific keywords.
* **Lexical Complexity:** Measures the average character length of all processed words.
* **Error Resilience:** Built-in safeguards against `FileNotFoundError` (missing text files) and `ZeroDivisionError` (empty documents).

## Prerequisites
Ensure you have Python 3.x installed on your computer.

## File Structure
The project directory contains the following files in the same folder:
```text
├── pythonAssessment.py   # The script containing the analyzer logic
└── article.txt           # The target text file you want to analyze
