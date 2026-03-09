Tool: Web Search

Purpose:
Search the web for up-to-date information, news, research papers, and authoritative sources.

Usage:
```
search(query="{{search_query}}", max_results={{max_results}}, date_filter="{{date_range}}")
```

Parameters:
- query: The search string (be specific and use quotation marks for exact phrases)
- max_results: Number of results to retrieve (default: 10)
- date_filter: Optional date range filter (e.g., "past_year", "past_month")

Best practices:
- Use specific, targeted queries rather than broad terms
- Include site: operator to search within specific domains
- Combine with scraper tool to extract full content from results
- Always verify information across multiple sources

Output:
- List of URLs with titles and snippets
- Relevance scores per result
