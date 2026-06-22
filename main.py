from src.agents.orchestrator import Orchestrator

if __name__ == "__main__":
    orchestrator = Orchestrator()
    result = orchestrator.run("Latest AI trends in 2026")
    print(result['report'])