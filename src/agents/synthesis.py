from typing import List, Dict
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class SynthesisAgent:
    def __init__(self, model_name: str = "gpt-4o-mini"):
        self.llm = ChatOpenAI(model=model_name, temperature=0.2)
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a world-class Research Analyst. Your task is to synthesize the following research data into a comprehensive, coherent, and professional Markdown report. "
                       "Ensure you include proper citations using [Source Title](URL) format. "
                       "Organize the report with clear headings, bullet points, and a summary section."),
            ("user", "User Query: {query}\n\nResearch Data:\n{data}")
        ])
        self.chain = self.prompt | self.llm | StrOutputParser()

    def synthesize(self, query: str, research_data: List[Dict]) -> str:
        """Synthesize research data into a markdown report using LLM."""
        if not research_data:
            return "No research data found to synthesize."
            
        formatted_data = ""
        for item in research_data:
            formatted_data += f"Title: {item.get('title', 'N/A')}\n"
            formatted_data += f"Content: {item.get('content', 'N/A')}\n"
            formatted_data += f"URL: {item.get('url', 'N/A')}\n\n"
        
        return self.chain.invoke({"query": query, "data": formatted_data})