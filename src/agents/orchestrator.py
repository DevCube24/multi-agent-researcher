from typing import TypedDict, List, Dict
from langgraph.graph import StateGraph, END
from src.agents.researcher import ResearcherAgent
from src.agents.synthesis import SynthesisAgent

class AgentState(TypedDict):
    query: str
    research_data: List[Dict]
    report: str

class Orchestrator:
    def __init__(self):        self.researcher = ResearcherAgent()
        self.synthesis = SynthesisAgent()
        self.workflow = self._create_workflow()

    def _create_workflow(self):
        workflow = StateGraph(AgentState)
        
        workflow.add_node("research", self._research_step)
        workflow.add_node("synthesize", self._synthesize_step)
        
        workflow.set_entry_point("research")
        workflow.add_edge("research", "synthesize")
        workflow.add_edge("synthesize", END)
        
        return workflow.compile()

    def _research_step(self, state: AgentState):
        results = self.researcher.research(state['query'])
        return {"research_data": results}

    def _synthesize_step(self, state: AgentState):
        report = self.synthesis.synthesize(state['research_data'])
        return {"report": report}

    def run(self, query: str):
        return self.workflow.invoke({"query": query})