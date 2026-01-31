def instruction_response_prompt(domain: str, n_samples: int) -> str:
    return f"""
You are an SEO content dataset generator.

Generate {n_samples} SEO-optimized instruction samples in the domain of {domain}.

STRICT RULES:
- Use the schema: instruction, input, output
- Output must be concise (2-3 lines, max 100 words)
- Output must start by mentioning the input keyword
- Use clear, search-friendly language
- No markdown, no code blocks
- No newlines inside JSON strings
- Output strictly valid JSON array

Example schema:
[
  {{
    "instruction": "Explain this model architecture.",
    "input": "Transformer Encoder",
    "output": "A transformer encoder processes input sequences in parallel using self-attention and feed-forward layers to create contextual embeddings. It is widely used in NLP models like BERT for capturing long-range dependencies efficiently."
  }}
]
"""
