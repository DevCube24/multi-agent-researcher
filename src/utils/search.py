from duckduckgo_search import DDGS
from typing import List, Dict
from src.utils.llm import call_llm
import json

def duckduckgo_search(query: str, max_results: int = 5) -> List[Dict]:
    """Perform a real web search using DuckDuckGo."""
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

def rank_results(query: str, results: List[Dict]) -> List[Dict]:
    """Rank results based on relevance using LLM."""
    prompt = f"""
    Query: {query}
    
    Results:
    {json.dumps(results, indent=2)}
    
    Rank the above results by relevance to the query. Return only the ranked list of indices (0-indexed) as a comma-separated string, most relevant first. 
    Example: 2,0,1
    """
    ranking_str = call_llm(prompt, system_prompt="You are a research assistant that ranks search results.")
    try:
        indices = [int(i.strip()) for i in ranking_str.split(",")]
        ranked_results = [results[i] for i in indices if i < len(results)]
        return ranked_results
    except Exception:
        # Fallback to length-based ranking if LLM fails
        return sorted(results, key=lambda x: len(x.get('content', '')), reverse=True)
