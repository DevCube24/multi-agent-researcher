from typing import List, Dict
from src.utils.search import duckduckgo_search, filter_results

class ResearcherAgent:
    def __init__(self, model_name: str = "gpt-4o-mini"):
        self.model_name = model_name

    def research(self, query: str) -> List[Dict]:
        """Perform research on a given query."""
        raw_results = duckduckgo_search(query)
        filtered_results = filter_results(raw_results)
        return filtered_results