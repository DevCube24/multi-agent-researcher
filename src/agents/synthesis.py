from typing import List, Dict
from src.utils.llm import call_llm

class SynthesisAgent:
    def __init__(self, model_name: str = "gpt-4o-mini"):
        self.model = model_name
        self.system_prompt = (
            "You are a world-class Research Analyst. Your task is to synthesize the following research data into a comprehensive, coherent, and professional Markdown report. "
            "Ensure you include proper citations using [Source Title](URL) format. "
            "Organize the report with clear headings, bullet points, and a summary section."
        )

    def synthesize(self, query: str, research_data: List[Dict]) -> str:
        """Synthesize research data into a markdown report using the LLM utility."""
        if not research_data:
            return "No research data found to synthesize."
            
        formatted_data = ""
        for item in research_data:
            formatted_data += f"Title: {item.get('title', 'N/A')}\n"
            formatted_data += f"Content: {item.get('content', 'N/A')}\n"
            formatted_data += f"URL: {item.get('url', 'N/A')}\n\n"
        
        user_prompt = f"User Query: {query}\n\nResearch Data:\n{formatted_data}"
        
        report = call_llm(
            prompt=user_prompt,
            model=self.model,
            system_prompt=self.system_prompt
        )
        
        return report

    def save_report(self, report: str, filename: str):
        """Placeholder for saving report to file system or database."""
        # Logic to be implemented in future runs or in a dedicated service
        pass