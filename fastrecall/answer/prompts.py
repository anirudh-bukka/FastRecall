"""Prompt templates for optional LLM answer generation.

FastRecall should work without LLM answer generation. These prompts are
placeholders for a later optional layer.
"""


ANSWER_PROMPT_TEMPLATE = """\
You are answering a question using retrieved evidence.

Question:
{query}

Evidence:
{evidence}

Answer with clear source references.
"""


COMPARISON_PROMPT_TEMPLATE = """\
Compare the repositories using the retrieved evidence.

Question:
{query}

Repository evidence:
{evidence}
"""

