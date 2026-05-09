# Language Parsers

This folder contains language-specific code parsers.

## Planned Languages

- `python_parser.py`: use Python's built-in `ast`.
- `java_parser.py`: begin with simple parsing, optionally use tree-sitter later.
- `perl_parser.py`: begin with regex-based package/sub/use extraction.
- `robot_parser.py`: parse Robot Framework suites, test cases, keywords,
  variables, resources, and tags.

## Output

Each parser should return records or intermediate objects that can become:

- `SymbolRecord`;
- `EdgeRecord`;
- `ChunkRecord`.

Keep parsers small and replaceable. Do not force every language into the same
exact implementation style.

