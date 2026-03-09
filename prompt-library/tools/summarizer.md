Tool: Summarizer

Purpose:
Condense long documents, articles, or datasets into concise, structured summaries.

Usage:
```
summarize(content="{{content}}", length="{{summary_length}}", focus="{{focus_areas}}")
```

Parameters:
- content: The text or document to summarize
- length: Target summary length — "short" (1–3 sentences), "medium" (1 paragraph), "long" (detailed)
- focus: Optional list of topics or aspects to prioritize in the summary

Best practices:
- Specify focus areas to avoid generic summaries
- Use "long" length for technical documents requiring full coverage
- Always ask for key takeaways to be listed separately
- Request source citations to be preserved in the summary

Output:
- Summary text
- Key takeaways (bullet list)
- Important quotes or data points retained
