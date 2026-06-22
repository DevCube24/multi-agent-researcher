from typing import List, Dict

class SynthesisAgent:
    def __init__(self, model_name: str = "gpt-4o-mini"):
        self.model_name = model_name

    def synthesize(self, research_data: List[Dict]) -> str:
        """Synthesize research data into a markdown report."""
        report = "# Research Report\n\n"
        for item in research_data:
            report += f"## {item['title']}\n"
            report += f"{item['content']}\n"
            report += f"Source: {item['url']}\n\n"
        return report