# Document Indexing

This folder indexes long-form documents using page and hierarchy structure.

## Responsibilities

- parse documents into text/page structures;
- detect headings, sections, paragraphs, tables, and figure references;
- create `PageNode` and `ChunkRecord` records;
- link parent/child and neighboring nodes;
- create placeholder summary nodes.

## Files

- `parser.py`: document parsing entrypoints.
- `page_index.py`: page node creation and neighbor linking.
- `hierarchy.py`: section/heading tree helpers.
- `summaries.py`: document/page/section summary placeholders.

## Flow

DocumentRecord -> parse -> pages/sections -> PageNode tree -> hierarchy index
-> storage.

Do not blindly chunk documents into embeddings. Preserve document structure
first. Embeddings can be added later as optional support.

