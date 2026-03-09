Tool: Data Extractor

Purpose:
Extract structured data (entities, facts, numbers, dates, relationships) from unstructured text.

Usage:
```
extract(content="{{content}}", schema="{{output_schema}}", confidence_threshold={{threshold}})
```

Parameters:
- content: The unstructured text to extract from
- schema: JSON schema defining the fields to extract
- confidence_threshold: Minimum confidence to include an extraction (0.0–1.0, default: 0.7)

Best practices:
- Provide a clear schema so the extractor knows what to look for
- Set confidence_threshold higher (0.85+) for critical data
- Always validate extracted numbers and dates against source text
- Combine with web-search tool to enrich extracted data

Output:
- Structured JSON matching the provided schema
- Confidence scores per extracted field
- Unmatched fields flagged as null with reason
