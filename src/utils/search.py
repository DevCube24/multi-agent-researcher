from duckduckgo_search import DDGS
from typing import List, Dict

def duckduckgo_search(query: str, max_results: int = 5) -> List[Dict]:
    """
    Perform a real web search using DuckDuckGo.
    Free and requires no API key.
    """
    print(f"Searching DuckDuckGo for: {query}")
    results = []
    with DDGS() as ddgs:
        ddgs_gen = ddgs.text(query, max_results=max_results)
        for r in ddgs_gen:
            results.append({
                "title": r.get("title"),
                "url": r.get("href"),
                "content": r.get("body")
            })
    return results

def filter_results(results: List[Dict]) -> List[Dict]:
    """Filter and rank results based on relevance (simple length-based ranking for now)."""
    return sorted(results, key=lambda x: len(x.get('content', '')), reverse=True)