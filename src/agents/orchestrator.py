from typing import TypedDict, List, Dict
from langgraph.graph import StateGraph, END
from src.agents.researcher import ResearcherAgent
from src.agents.synthesis import SynthesisAgent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

class AgentState(TypedDict):
    query: str
    plans: List[str]
    research_data: List[Dict]
    report: str

class Orchestrator:
    def __init__(self):
        self.researcher = ResearcherAgent()
        self.synthesis = SynthesisAgent()
        self.llm = ChatOpenAI(model="gpt-4o-mini")
        self.workflow = self._create_workflow()

    def _create_workflow(self):
        workflow = StateGraph(AgentState)
        
        workflow.add_node("planner", self._plan_step)
        workflow.add_node("research", self._research_step)
        workflow.add_node("synthesize", self._synthesize_step)
        
        workflow.set_entry_point("planner")
        workflow.add_edge("planner", "research")
        workflow.add_edge("research", "synthesize")
        workflow.add_edge("synthesize", END)
        
        return workflow.compile()

    def _plan_step(self, state: AgentState):
        prompt = ChatPromptTemplate.from_template(
            "Break down the following research query into 3-5 specific sub-tasks or search queries. "
            "Return each query on a new line.\n\nQuery: {query}"
        )
        chain = prompt | self.llm
        response = chain.invoke({"query": state['query']})
        plans = [p.strip() for p in response.content.split('\n') if p.strip()]
        return {"plans": plans}

    def _research_step(self, state: AgentState):
        all_results = []
        for sub_query in state.get('plans', [state['query']]):
            results = self.researcher.research(sub_query)
            all_results.extend(results)
        return {"research_data": all_results}

    def _synthesize_step(self, state: AgentState):
        report = self.synthesis.synthesize(state['query'], state['research_data'])
        return {"report": report}

    def run(self, query: str):
        return self.workflow.invoke({"query": query})