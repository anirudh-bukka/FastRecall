# Answer Composition

This folder turns retrieval results into user-facing answers.

## Responsibilities

- group retrieval evidence;
- select relevant snippets;
- format citations to files, symbols, pages, or documents;
- produce comparison answers for multi-repo queries;
- keep answer composition separate from retrieval.

## Files

- `composer.py`: answer-building functions.
- `prompts.py`: optional prompt templates if an LLM is later used.

## Flow

RetrievalResult list -> evidence grouping -> answer structure -> final text.

The first implementation can be extractive and deterministic. LLM-based answer
generation can be optional later.

