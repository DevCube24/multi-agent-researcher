from typing import List, Dict
from src.utils.search import duckduckgo_search, rank_results

class ResearcherAgent:
    def __init__(self, model_name: str = "gpt-4o-mini"):
        self.model_name = model_name

    def research(self, query: str) -> List[Dict]:
        """Perform research on a given query with LLM-based ranking."""
        raw_results = duckduckgo_search(query)
        ranked_results = rank_results(query, raw_results)
        return ranked_results
